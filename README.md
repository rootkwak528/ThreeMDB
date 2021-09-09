# ThreeMDB

# three.js를 활용한 3차원 영화 추천 서비스

![image-20210802001427716](README.assets/image-20210802001427716.png)

<br>

## 목차

[1. ThreeMDB 소개](#1-ThreeMDB-소개)

[2. 개요](#2-개요)

[3. 기술스택 및 개발환경](#3-기술스택-및-개발환경)

[4. 기능 소개](#4-기능-소개)

​		[4.1. 계정 로그인 및 회원가입](#4-1-계정-로그인-및-회원가입)

​		[4.2. 영화 검색](#4-2-영화-검색)

​		[4.3. 3차원 UI의 영화 추천](#4-3-3차원-UI의-영화-추천)

​		[4.4. 리뷰 작성](#4-4-리뷰-작성)

[5. 개발 이슈](#5-개발-이슈)

​		[5.1. three.js 사용](5-1-three-js-사용)

​		[5.2. ERD 및 movie 데이터](#5-2-ERD-및-movie-데이터)

​		[5.3. 상세 페이지 모달](#5-3-상세-페이지-모달)

​		[5.4. three.js 사용](#5-4-async-await-비동기-처리)

[6. 실행 방법](#6-실행-방법)

<br><br>

## 1. ThreeMDB 소개

* 기간 : 2021.05.20 - 2021.05.28
* 인원 : 곽호근 (팀장 / Three.js, 배포), 정훈규 (Backend, Frontend)
* 주제 : three.js를 활용한 3차원 영화 추천 웹 서비스
* 소스코드 : [백엔드](https://github.com/rootkwak528/BE-ThreeMDB#1-threemdb-%EC%86%8C%EA%B0%9C) / [프론트엔드](https://github.com/rootkwak528/FE-ThreeMDB)

<br><br>

## 2. 개요

[<img src="https://www.themoviedb.org/assets/2/v4/logos/v2/blue_short-8e7b30f73a4020692ccca9c88bafe5dcb6f8a62a4c6bc55cd9ba82bb2cd95f6c.svg" alt="tmdb-logo" style="zoom: 33%;" />](https://developers.themoviedb.org/3)

[TMDB](https://themoviedb.org)는 전세계에서 가장 큰 규모의 영화 DB를 훌륭한 [API](https://developers.themoviedb.org/3)로 공개하고 있습니다. **TMDB의 기본 추천 API를 3D UI에서 구현한다면, 같은 기능으로도 색다른 UX를 제공할 수 있지 않을까요?** 이러한 아이디어에서 이번 프로젝트는 시작되었습니다.

<br><br>

## 3. 기술스택 및 개발환경

### 기술스택

* **BackEnd :** ![django](https://img.shields.io/badge/django-3.2.3-green)![drf](https://img.shields.io/badge/drf-3.12.4-green)![drf-jwt](https://img.shields.io/badge/drf_jwt-1.11.0-green)
* **FrontEnd :** ![vue.js](https://img.shields.io/badge/vue.js-2.6.11-green)![vuex](https://img.shields.io/badge/vuex-3.6.2-green)![bootstrap](https://img.shields.io/badge/bootstrap-5.0.1-green.svg)![three.js](https://img.shields.io/badge/three.js-0.128.0-green.svg) 
* **Deploy :** ![heroku](https://img.shields.io/badge/heroku--orange)![netlify](https://img.shields.io/badge/netlify--orange)

<br>

### 개발환경

* macOS Big Sur 11.3.1 & Windows 10
* Visual Studio Code 1.57.0
* Python 3.8.6
* Node.js 14.16.1

<br><br>

## 4. 기능 소개

### 4.1. 계정 로그인 및 회원가입

![readme-login](README.assets/readme-login.gif)

> 리뷰 및 댓글 작성 등 커뮤니티 기능을 위한 계정을 구현했습니다. **사용자 인증은 JWT**로 진행됩니다.

<br>

### 4.2. 영화 검색

![readme-search](README.assets/readme-search.gif)

> 영화 추천 페이지로 이동하기 위해 최초에 관심 영화 3편을 선정합니다. **TMDB에 등록된 영화는 모두 검색 가능**합니다. 영화 포스터에 마우스 오버 시 툴팁으로 제목을 보여주고, 선택한 영화를 재선택하면 영화 선택이 해제됩니다.

<br>

### 4.3. 3차원 UI의 영화 추천

![readme-recommend](README.assets/readme-recommend.gif)

> 키보드와 마우스 입력으로 3차원 공간을 자유롭게 이동하며, **좋아하는 영화를 선택하여 관련 영화들을 추천** 받을 수 있습니다. 새롭게 추천된 영화들은 선택된 영화의 z축 뒷편에 추가되며, 탐색을 거듭할 수록 z축으로 깊은 형태가 됩니다.
>
> 가려진 포스터도 잘 보일수 있도록 **마우스 오버 시, 포스터의 layer depth가 0이 되어** 다른 포스터에 가려지지 않고 제일 앞에 보이게 됩니다.
>
> 표시되는 영화의 수에 이론적인 제한은 없으며, 맥북 프로 2017년 모델에서 테스트 했을 때, 500개 이상 표시해도 성능 저하 없이 잘 작동했습니다.

<br>

### 4.4. 리뷰 작성

![readme-review](README.assets/readme-review.gif)

> 영화 추천 페이지에서 영화 포스터를 Ctrl+클릭 하면 영화의 상세 페이지가 팝업됩니다. 상세 페이지에서는 **평점과 리뷰 그리고 댓글을** 작성할 수 있습니다.

<br><br>

## 5. 개발 이슈

### 5.1. three.js 사용

[<img src="https://miro.medium.com/max/724/1*aDcnXab1QC_5KF8JUxDEYA.png" alt="three.js-logo" style="zoom:33%;" />](https://threejs.org/)

**[three.js](https://threejs.org/)는 WebGL 엔진에 기반한 JavaScript 3D library로, 훌륭한 [공식 문서](https://threejs.org/docs/index.html#manual/en/introduction/Creating-a-scene)와 [다양한 레퍼런스](https://threejs.org/examples/)를 갖고 있습니다.**

three.js는 3차원 공간을 구현하기 위해 일반적인 웹에서 사용되지 않는 개념들을 다수 포함하고 있습니다.

라이브러리는 객체지향적으로 작성되었으며, 가장 주요한 세가지 객체는 Scene, Camera, Renderer입니다.

먼저, Scene은 화면에 표시하고자 하는 모든 3차원 객체를 포함하는 객체입니다.

Camera는 실시간으로 Scene을 촬영하는 객체로서 Controller를 통해 사용자의 입력에 따라 움직이도록 구현할 수 있습니다.

마지막으로 Renderer는 Camera가 촬영한 장면을 클라이언트 화면에 출력하는 객체입니다.

<br>

아래는 본 프로젝트에서 작성된 **[three.js 코드](https://github.com/rootkwak528/FE-ssafy-final-pjt/blob/master/src/views/movies/MovieRecommend.vue)의 개략적 의사코드입니다.**

``` 
init()

// three.js 초기화
function init () {

	씬 생성
	카메라 생성
	렌더러 생성
	
	// 웹 화면에 출력하기 위함
	DOM에 렌더러 추가
	
	조명 및 3D 메쉬 생성
	씬에 조명 및 3D 메쉬 추가
	
  // 사용자 인풋에 반응하기 위함
	컨트롤러 생성
	씬에 컨트롤러 추가
	
	animate()
	
}

// three.js 애니메이션 생성
// 비동기로 작동하는 requestAnimationFrame()를 재귀적으로 호출하기 때문에 (이론 상 60 calls/s)
// 사용자 인풋이나 데이터 변화를 거의 실시간으로 반영할 수 있습니다.
// - requestAnimationFrame()은 Web API의 내장함수입니다.
function animate () {

	requestAnimationFrame( animate )
	
}
```

<br><br>

### 5.2. ERD 및 movie 데이터

![ERD](./README.assets/image-20210527180344809.png)

영화 검색과 추천은 모두 **TMDB API**를 사용하기 때문에 **movies 테이블은 최초에 빈 테이블입니다.**

movies 테이블이 사용되는 순간은 사용자가 별점을 매기거나 리뷰를 남기는 등의 행위를 할 때입니다.

**따라서 사이트의 영화 상세 페이지에 접속하는 순간, 클라이언트는 영화 정보를 request body에 담아 서버에 조회 요청을 보내고, 서버는 상황에 따라 두가지 다른 경로로 응답을 보내옵니다.**

1. 만약 DB에 해당 영화의 레코드가 있다면, 바로 DB에서 레코드를 불러와 응답 메시지에 담아 전송합니다.
2. 하지만 DB에 해당 영화의 레코드가 없다면, 먼저 TMDB 서버에 영화 데이터를 요청하고, 응답 받은 데이터를 DB에 저장하고 동시에 DB에 저장한 데이터를 응답 메시지에 담아 전송합니다.

<br>

아래는 관련된 [View 함수 코드](https://github.com/rootkwak528/BE-ssafy-final-pjt/blob/master/movies/views.py)입니다.

> Django는 MVC 패턴의 변형인 MTV 패턴을 사용하기 때문에 여기서 View는 MVC 패턴의 Controller에 해당합니다.

```python
# BE/movies/views.py

@api_view(['POST'])
def movie_create(request):

    movie_id = request.data.get('id')
    movie = Movie.objects.filter(movie_id=movie_id)

    # 영화 정보가 DB에 없는 경우 DB에 저장
    if not movie.exists():
        movie_data = {
            'movie_id': movie_id,
            'title': request.data.get('title'),
            'overview': request.data.get('overview'),
            'release_date': request.data.get('release_date'),
            'poster_path': request.data.get('poster_path'),
        }
        
        serializer = MovieSerializer(data=movie_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    # 영화 정보가 DB에 있는 경우 DB에서 데이터 로드
    else:
        try:
          	# 리뷰와 댓글 데이터도 한번에 반환하여 DB 요청 횟수 최적화
            reviews = Review.objects.select_related('user')
            comments = Comment.objects.select_related('user')

            movie = Movie.objects.prefetch_related(
                Prefetch('reviews', queryset=reviews),
                Prefetch('reviews__comments', queryset=comments)
                ).get(pk=movie[0].pk)

        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
```

<br><br>

### 5.3. 상세 페이지 모달

최초에는 영화 상세 페이지를 별도 url로 라우팅하여 구현하려 했습니다.

3차원 상의 영화 추천 목록을 돌아다니다 영화 카드를 클릭하면 상세 페이지로 넘어가는 방식이었습니다.

그러나 이렇게 되면 **상세 페이지에 방문했다 영화 추천 페이지로 되돌아올 때 3차원 Scene이 초기화되는 문제가 있었습니다.**

이는 UX 측면에서는 사용자가 탐색을 반복해야 하기 때문에 낭비를 발생시키는 큰 문제였습니다.

<br>

데이터를 유지하려면 두가지 옵션이 가능해보였습니다.

클라이언트에 임시로 데이터를 저장하거나, 서버에 데이터를 저장하는 방식이었습니다.

하지만 3차원 Scene을 모두 유지하려면 문자열로 1천만~ 수억 사이즈였는데, 클라이언트 로컬 스토리지 최대 사이즈인 5MB를 초과하는 사이즈였습니다. (출처 : https://web.dev/storage-for-the-web/)

또한 서버에 비정형 데이터를 저장하려면 SQLite 외에 새로운 DB를 추가해야 하고, 상세 페이지에 방문할 때마다 수십~수백 MB의 큰 데이터를 주고받아야 한다는 문제점이 있었습니다.

<br>

결론적으로 사용자 입장에서도 익숙한 **모달창으로 상세 페이지를 구현해, url 이동을 없애고 Scene 데이터를 보존했습니다.**

<br>

![image-20210527193220115](README.assets/image-20210527193220115.png)

> 모달창으로 구현된 영화 상세 페이지의 모습.
>
> 모달창으로 바꾸고 또 좋았던 점은 연습 삼아 구현한 후처리 기능을 포함시킬 수 있었다는 점입니다. 덕분에 모달창 뒤의 3차원 영화 추천 목록을 다크모드처럼 표현해 화면 전환 효과를 더 극대화했습니다.

<br><br>

### 5.4. async-await 비동기 처리

**axios**는 비동기적으로 요청과 응답을 처리해주는 **Promise** 기반의 함수로, 일반적인 경우라면 **axios**를 도입하는 것만으로 비동기를 처리하기 부족함이 없을 것입니다.

하지만 이 프로젝트에서는 **vuex**와 **three.js**를 도입했기 때문에 **axios**와 데이터가 서로 다른 파일에 위치하면서 작동이 틀어졌습니다. **axios**는 **vuex**의 `index.js` 에서 실행됐지만, 바꿔야 하는 데이터는 추천 컴포넌트 파일 내에 위치하고 있습니다.

<br>

다른 컴포넌트에서 사용하는 일이 없기 때문에 데이터를 **state**로 처리하는 것은 비효율적이었습니다. 따라서 기존의 코드도 헤치지 않고 간단히 **async-await**로 **dispatch** 코드를 비동기 처리하여 문제를 해결했습니다.

이 예시 외에도 다양한 코드에서 이와 같이 비동기 처리를 실시해 오류를 피해갈 수 있었습니다.

![image-20210617164711965](README.assets/image-20210617164711965.png)

> **axios**만 사용하면, 응답을 받기 전에 데이터를 확인하고 3D 씬을 구성하기 때문에 추천 목록이 표시되지 않습니다.

<br>

![image-20210617164612300](README.assets/image-20210617164612300.png)

> **async await** 코드를 추가하자, HTTP 응답과 데이터 확인이 비동기적으로 일어나 3D 씬이 올바르게 생성되었습니다.

<br>

아래는 관련된 [컴포넌트](https://github.com/rootkwak528/FE-ssafy-final-pjt/blob/master/src/views/movies/MovieRecommend.vue)와 [vuex](https://github.com/rootkwak528/FE-ssafy-final-pjt/blob/master/src/store/index.js)의 코드 일부분입니다.

```js
// FE/src/views/movies/MovieRecommend.vue

async recommend ( movieId, position ) {
  await this.getRecommends( movieId )
  if ( this.movieRecommends ) {
  	this.updateGeometriesToScene( this.movieRecommends, position )
  }
}
```

```js
// FE/src/store.index.js

async getRecommends ({ commit }, movieId) {
  const url = `https://api.themoviedb.org/...`
  await axios({
    url: url,
    method: 'get',
  })
    .then( res => {
      if (res.data.results) {
        commit('SET_MOVIE_RECOMMENDS', res.data.results)
      } else {
        commit('SET_MOVIE_RECOMMENDS', null)
      }
    })
    .catch( err => {
      console.log(err)
      commit('SET_MOVIE_RECOMMENDS', null)
    })
},
```

<br><br>

## 6. 실행 방법

### [BackEnd](https://github.com/rootkwak528/BE-ThreeMDB)

1. 라이브러리를 설치합니다.

```
pip install -r requirements.txt
```

2. DB를 마이그레이션 합니다.

```
python manage.py migrate
```

3. 서버를 실행합니다.

``` 
python manage.py run server
```

<br>

### [FrontEnd]((https://github.com/rootkwak528/FE-ThreeMDB))

1. 라이브러리를 설치합니다.

```
npm i
```

2. 서버를 실행합니다.

```
npm run serve
```

<br><br>

**Fin.**