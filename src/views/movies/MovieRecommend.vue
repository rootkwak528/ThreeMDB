<template>
  <div id="container">

    <div id="info">
      <span>
        <b>WASD</b> move, 
        <b>R|F</b> up | down, 
        <b>Q|E</b> roll, 
        <b>DRAG</b> pitch&yaw, 
        <b>Ctrl + CLICK</b> detail,  
        <b>Shift + CLICK</b> recommend,
        <b>Spacebar</b> home
      </span>
		</div>

    <div v-if="isDetail">
      <DetailCard
        :selectedMovie="selectedMovie"
        @close-detail="closeDetail"
      />
    </div>

  </div>
</template>

<script>
import DetailCard from '@/components/Recommend/DetailCard'

import * as THREE from 'three'
import { FlyControls } from 'three/examples/jsm/controls/FlyControls'
import { BufferGeometryUtils } from 'three/examples/jsm/utils/BufferGeometryUtils'

// post-processing
import { EffectComposer } from 'three/examples/jsm/postprocessing/EffectComposer.js';
import { RenderPass } from 'three/examples/jsm/postprocessing/RenderPass.js';
import { ShaderPass } from 'three/examples/jsm/postprocessing/ShaderPass.js';

import { RGBShiftShader } from 'three/examples/jsm/shaders/RGBShiftShader.js';
import { DotScreenShader } from 'three/examples/jsm/shaders/DotScreenShader.js';

// import results from '@/data/movies' // this is for test
import axios from 'axios'

const TMDB_API_KEY = process.env.VUE_APP_TMDB_API_KEY
const SERVER_URL = process.env.VUE_APP_SERVER_URL

// scene 변수
let container
let camera, controls, scene, renderer
let pickingTexture, pickingScene
let highlightBox
let composerZizizik // post-processing

// 마우스 가리키는 카드 판별 변수
let pickingData, pointer

// data 변수
let pointedCardId = null
let clicked = false
let shiftDown = false
let ctrlDown = false

// Fly Controls 변수
const clock = new THREE.Clock()

// style
// const navbarDOM = document.querySelector('#nav')
// const infoDOM = document.querySelector('#info')

export default {
  name: 'MovieRecommend',
  components: {
    DetailCard,
  },

  data () {

    return {
      // index 페이지에서 받아오는 데이터
      likedMovies: [],

      // three.js
      isDetail: false,
      selectedMovie: null,
      movieObject: {}, // this is for test
      movieLength: 0,
    }

  },

  mounted () {

    // index 페이지에서 받아오는 데이터
    const likedMoviesJson = localStorage.getItem('likedMovies')
    this.likedMovies = JSON.parse(likedMoviesJson)

    // console.log(this.likedMovies)

    const infobar = document.getElementById( 'info' )
    const infobarHeight = infobar.offsetHeight
    infobar.style.top = `${window.innerHeight - infobarHeight}px`

    // three.js
    this.main()

    // console.log(this.likedMovies)

    this.getRecommendations( this.likedMovies[1].id, new THREE.Vector3(     0, 0, -1000 ) )
    this.getRecommendations( this.likedMovies[0].id, new THREE.Vector3( -1800, 0, -1000 ) )
    this.getRecommendations( this.likedMovies[2].id, new THREE.Vector3(  1800, 0, -1000 ) )

  },

  methods: {

    main () {

			this.init()
			this.animate()

    },

    init () {

      container = document.getElementById( 'container' );

      // // 씬
      // this.initScene()

      // 씬 초기화
      scene = new THREE.Scene();
      scene.background = new THREE.Color( 0xffffff );
      // scene.background.setStyle( "rgba(100, 98, 98, 0.5)" )

      // 마우스 가리키는 씬
      pickingScene = new THREE.Scene();
      pickingTexture = new THREE.WebGLRenderTarget( 1, 1 );

      // 재질 로더
      // loader = new THREE.TextureLoader()

      // 조명 1
      scene.add( new THREE.AmbientLight( 0x555555 ) );

      // 조명 2
      const light = new THREE.SpotLight( 0xffffff, 1.5 );
      light.position.set( 0, 500, 2000 );
      scene.add( light );

      // 영화 데이터 확인
      // const movies = results.results // this is for test

      // 영화 확인 전 피킹 데이터 초기화
      pickingData = []
      pointer = new THREE.Vector2()

      // 포스터 카드 geometry 추가
      // this.updateGeometriesToScene( movies )
      this.updateGeometriesToScene( this.likedMovies.slice( 0, 1 ), new THREE.Vector3( -400, 0, 0 ), new THREE.Vector3( 0, 0, 0 ) )
      this.updateGeometriesToScene( this.likedMovies.slice( 1, 2 ), new THREE.Vector3(    0, 0, 0 ), new THREE.Vector3( 0, 0, 0 ) )
      this.updateGeometriesToScene( this.likedMovies.slice( 2, 3 ), new THREE.Vector3(  400, 0, 0 ), new THREE.Vector3( 0, 0, 0 ) )

      // 포인터 가르키는 박스에 씌울 하이라이트 박스도 Scene에 추가
      highlightBox = new THREE.Mesh(

        this.getHighlightGeometry(),
        new THREE.MeshBasicMaterial( { color: 0xffff00, depthTest: false }

        ) );
      highlightBox.renderOrder = 1
      scene.add( highlightBox );

      // 카메라
      camera = new THREE.PerspectiveCamera( 70, window.innerWidth / window.innerHeight, 1, 10000 );
      camera.rotation.x = 0.0367464081048994
      // camera.rotation.x = 0.1367464081048994
      // camera.rotation.y = -0.07590929642410132
      // camera.rotation.z = 0.013967953561495515
      // camera.position.x = -50.64439864745512
      // camera.position.y = -89.17068354000168
      // camera.position.z = 97.64381447381723

      camera.layers.enable(1)

      // 렌더러 화면에 추가
      renderer = new THREE.WebGLRenderer( { antialias: true } );      
      renderer.setPixelRatio( window.devicePixelRatio );
      renderer.setSize( window.innerWidth, window.innerHeight );
      container.appendChild( renderer.domElement );

      // post-process #1 디테일 페이지 뒤에 지직 거리는 효과
      {
        composerZizizik = new EffectComposer( renderer );
        composerZizizik.addPass( new RenderPass( scene, camera ) );

        const effect1 = new ShaderPass( DotScreenShader );
        effect1.uniforms[ 'scale' ].value = 100;
        composerZizizik.addPass( effect1 );

        const effect2 = new ShaderPass( RGBShiftShader );
        effect2.uniforms[ 'amount' ].value = 0.001;
        composerZizizik.addPass( effect2 );
      }
      
      // 컨트롤러 추가
      this.activateEventsAndControls()

    },

    updateGeometriesToScene ( movies, 
                              POS   = new THREE.Vector3( 0, 0, -1000 ), 
                              DIST  = new THREE.Vector3( 1500, 1000, 500 ) ) {

      // pickingScene 의 재질
      const pickingMaterial = new THREE.MeshBasicMaterial( { vertexColors: true } );

      // geometry 배열
      // const geometriesDrawn = [];
      const geometriesPicking = [];

      // 그외 변수
      const matrix = new THREE.Matrix4();
      const quaternion = new THREE.Quaternion();
      const color = new THREE.Color();

      movies.forEach( movie => {

        // 포스터 없으면 continue
        if (!movie.poster_path) {
          return
        }

        // 이미 리스트에 있으면 continue
        if (pickingData[ movie.id ]) {
          return
        }

        // movieObject에 데이터 저장
        this.movieObject[ movie.id ] = movie
        // this.movieObject[ movie.id ] = {
        //   ...movie,
        //   movie_id: movie.id,
        // }
        // delete this.movieObject[ movie.id ].id


        // movieLength 추가
        this.movieLength += 1
          
        // geometry 원형
        let geometry = this.getPosterGeometry()

        // Scene 의 재질에 texture image 적용할 TextureLoader
        const loadManager = new THREE.LoadingManager();
        const loader = new THREE.TextureLoader(loadManager);

        const posterTexture = loader.load(`https://www.themoviedb.org/t/p/w500${movie.poster_path}`)
        const posterMaterial = new THREE.MeshBasicMaterial({ map: posterTexture })
        const highlightMaterial = new THREE.MeshBasicMaterial({ map: posterTexture, depthTest: false })

        posterTexture.minFilter = THREE.LinearMipMapLinearFilter
        posterTexture.magFilter = THREE.LinearFilter
        
        // 위치 설정
        const position = new THREE.Vector3();
        position.x = POS.x + DIST.x * ( 1 - 2 * Math.random() );
        position.y = POS.y + DIST.y * ( 1 - 2 * Math.random() );
        position.z = POS.z + DIST.z * ( - Math.random() ) - 500;

        // 방향 설정
        const rotation = new THREE.Euler();
        rotation.x = 0;
        rotation.y = 0;
        rotation.z = 0;

        // 스케일 설정
        const scale = new THREE.Vector3();
        scale.x = 100;
        scale.y = 100;
        scale.z = 100;

        // 위치, 방향, 스케일 적용
        quaternion.setFromEuler( rotation );
        matrix.compose( position, quaternion, scale );
        geometry.applyMatrix4( matrix );

        // geometry를 마우스 가리키는 씬에 사용할 geometry 배열에 추가
        // 단, 컬러를 "id" (movie.id) 값으로 설정한다.
        const pickingGeometry = geometry.clone();
        this.applyVertexColors( pickingGeometry, color.setHex( movie.id ) );
        geometriesPicking.push( pickingGeometry );

        // 각 카드 별 데이터 저장
        pickingData[ movie.id ] = {

          position,
          rotation,
          scale,
          highlightMaterial,

        };

        loadManager.onLoad = () => {
          
          // Scene에 포스터 카드 추가
          const object = new THREE.Mesh( 

            // BufferGeometryUtils.mergeBufferGeometries( geometriesDrawn ), 
            geometry,
            posterMaterial,

            );


          scene.add( object );

        };
        
      }) // forEach end

      // 포인터 바라보는 Scene에도 포스터 카드 추가
      const pickingObejcts = new THREE.Mesh( 

        BufferGeometryUtils.mergeBufferGeometries( geometriesPicking ),
        pickingMaterial
        
        )
      pickingScene.add( pickingObejcts )

    },

    getCubeGeometry ( boxWidth, boxHeight, boxDepth ) {

      return new THREE.BoxGeometry(boxWidth, boxHeight, boxDepth);

    },

    getPosterGeometry () {

      return this.getCubeGeometry(2, 3, 0.03);

    },

    getHighlightGeometry () {

      return this.getCubeGeometry(2.3, 3.45, 0.0345);

    },

    // 카드 geometry 생성
    getCardGeometry () {

      const width = 2, height = 3;

      const shape = new THREE.Shape();
      shape.moveTo( 0,0 );
      shape.lineTo( 0, height );
      shape.lineTo( width, height );
      shape.lineTo( width, 0 );
      shape.lineTo( 0, 0 );

      const extrudeSettings = {

        steps: 1,
        depth: 0.01,
        bevelEnabled: true,
        bevelThickness: 0.03,
        bevelSize: 0.06,
        bevelSegments: 1

      };
      
      return new THREE.ExtrudeGeometry(shape, extrudeSettings)

    },

    // 컬러 적용
    applyVertexColors ( geometry, color ) {

      const position = geometry.attributes.position; // geometry.attributes 속성으로 위치 등에 접근할 수 있나보다.
      const colors = [];

      for ( let i = 0; i < position.count; i ++ ) {

        colors.push( color.r, color.g, color.b );

      }

      geometry.setAttribute( 'color', new THREE.Float32BufferAttribute( colors, 3 ) );

    },

    activateEventsAndControls () {

      // 이벤트리스너 추가
      renderer.domElement.addEventListener( 'pointermove', this.onPointerMove ) // 마우스 이동
      renderer.domElement.addEventListener( 'pointerdown', this.onPointerDown ) // 마우스 클릭
      document.addEventListener( 'keydown', this.onKeyDown ) // 키보드 down
      document.addEventListener( 'keyup', this.onKeyUp ) // 키보드 up

      // 컨트롤러 추가
      // 매번 실행하는 new ()는 논리적으로는 불필요한 과정이지만,
      // dragToLook을 true로 바꾸어도, 자동 회전되는 버그를 방지하기 위함
      controls = new FlyControls( camera, renderer.domElement )
      controls.movementSpeed = 1000
      controls.rollSpeed = Math.PI / 5
      controls.dragToLook = true

    },

    deactivateEventsAndControls () {

      // 이벤트리스너 제거
      renderer.domElement.removeEventListener( 'pointermove', this.onPointerMove ) // 마우스 이동
      renderer.domElement.removeEventListener( 'pointerdown', this.onPointerDown ) // 마우스 클릭
      document.removeEventListener( 'keydown', this.onKeyDown ) // 키보드 down
      document.removeEventListener( 'keyup', this.onKeyUp ) // 키보드 up 

      // 컨트롤러 비활성화
      controls.rollSpeed = 0.001
      controls.movementSpeed = 0
      controls.dragToLook = false
      
    },

    onPointerMove ( e ) {

      pointer.x = e.clientX;
      pointer.y = e.clientY;

    },

    onPointerDown ( ) {

      clicked = true

    },

    onKeyDown ( e ) {
      
      shiftDown = e.shiftKey
      ctrlDown  = e.ctrlKey

    },

    onKeyUp ( e ) {

      shiftDown = e.shiftKey
      ctrlDown  = e.ctrlKey

      if (e.key == " " || e.key == "Spacebar") {

        camera.rotation.x = 0.0367464081048994
        camera.rotation.y = 0
        camera.rotation.z = 0
        camera.position.x = 0
        camera.position.y = 0
        camera.position.z = 0
        // camera.rotation.x = 0.1367464081048994
        // camera.rotation.y = -0.07590929642410132
        // camera.rotation.z = 0.013967953561495515
        // camera.position.x = -50.64439864745512
        // camera.position.y = -89.17068354000168
        // camera.position.z = 97.64381447381723

      }

    },

    pick () {

      //render the picking scene off-screen

      // set the view offset to represent just a single pixel under the mouse

      camera.setViewOffset( renderer.domElement.width,
                            renderer.domElement.height, 
                            pointer.x * window.devicePixelRatio | 0, 
                            pointer.y * window.devicePixelRatio | 0, 
                            // (pointer.y - navbarHeight) * window.devicePixelRatio | 0, // navbar 사이즈만큼 위치 조절
                            1, 
                            1 );

      // render the scene

      renderer.setRenderTarget( pickingTexture );
      renderer.render( pickingScene, camera );

      // clear the view offset so rendering returns to normal

      camera.clearViewOffset();

      //create buffer for reading single pixel

      const pixelBuffer = new Uint8Array( 4 );

      //read the pixel

      renderer.readRenderTargetPixels( pickingTexture, 0, 0, 1, 1, pixelBuffer );

      //interpret the pixel as an ID

      pointedCardId = ( pixelBuffer[ 0 ] << 16 ) | ( pixelBuffer[ 1 ] << 8 ) | ( pixelBuffer[ 2 ] );
      const data = pickingData[ pointedCardId ];

      if ( data ) {

        //move our highlightBox so that it surrounds the picked object

        if ( data.position && data.rotation && data.scale ) {

          highlightBox.position.copy( data.position );
          highlightBox.rotation.copy( data.rotation );
          highlightBox.scale.copy( data.scale );
          highlightBox.material.copy( data.highlightMaterial );
          highlightBox.visible = true;

        } 

      } else {

        highlightBox.visible = false;

      }

    },

    async choice () {

      if ( clicked ) {
        
        clicked = false

        if ( pointedCardId ) {

          // recommend
          if ( shiftDown ) {

            console.log( 'shift +', pointedCardId )
            this.getRecommendations( pointedCardId,
                                     pickingData[ pointedCardId ].position )

          // detail
          } else if ( ctrlDown ) {

            console.log( 'ctrl +', pointedCardId )
            // console.log( this.movieObject[ pointedCardId ] )
            // this.exportScene() // 굉장히 비싼 작업
            
            // 디테일 창을 띄우기 전에 서버로부터 데이터 가져오기
            await axios({
              url: `${SERVER_URL}movies/`,
              method: 'post',
              data: this.movieObject[ pointedCardId ],
            })
              .then((res) => {
                this.selectedMovie = res.data
                // console.log('res.data:', res.data)
              })
              .catch((err) => {
                console.log(err)
              })

            this.isDetail = true
            this.deactivateEventsAndControls( pointedCardId )

            scene.background = new THREE.Color( 0x000000 );

            const navbarDOM = document.querySelector('#nav')
            const infoDOM = document.querySelector('#info')
            navbarDOM.style.display = 'none'
            infoDOM.style.display = 'none'

          }
        }
      }
    },

    getRecommendations ( movieId, position ) {

      axios({

        url: `https://api.themoviedb.org/3/movie/${movieId}/recommendations?api_key=${TMDB_API_KEY}&language=ko-KR&page=1`,
        method: 'get',

      })

        .then( res => {

          if (res.data.results) {

            const movies = res.data.results
            this.updateGeometriesToScene( movies, position )

          }
          
        })

        .catch( err => {

          console.log(err)

        })

    },

    animate () {

      // 비동기 함수
      requestAnimationFrame( this.animate );

      this.render();

    },

    render () {

      // Fly Controls
      controls.update( clock.getDelta() );

      this.pick();
      this.choice()

      if ( !this.isDetail ) {

        renderer.setRenderTarget( null );
        renderer.render( scene, camera );
        
      } else {

        composerZizizik.render()
        
      }

    },

    closeDetail () {

      this.isDetail = false
      this.activateEventsAndControls()

      clicked = false
      shiftDown = false
      ctrlDown = false

      scene.background = new THREE.Color( 0xffffff );

      const navbarDOM = document.querySelector('#nav')
      const infoDOM = document.querySelector('#info')
      navbarDOM.style.display = 'block'
      infoDOM.style.display = 'block'

    }
  }
}
</script>

<style>
#info b {
  color: orange
}

/* #info span {
  color: rgba( 255, 255, 255, 0.6 )
} */

#info {
  width: 100%;
  position: absolute;
  text-align: center;
  /* background-color: rgba( 255, 165, 0, 0.2 ); */
  backdrop-filter: blur(3px);
  box-shadow: 0 0 0.15rem 0 rgba(0, 0, 0, .1);
}

#nav {
  width: 100%;
  position: absolute;
  /* background-color: rgba( 255, 255, 255, 0.8 ); */
  backdrop-filter: blur(3px);
  box-shadow: 0 0 0.15rem 0 rgba(0, 0, 0, .1);
}

</style>