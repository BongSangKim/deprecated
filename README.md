# 객체지향 프로그래밍, Object-Oriented Programming (se271, 2017)

## 강의 개요

객체지향 프로그래밍은 객체지향 프로그래밍의 개념의 학습과 이러한 개념을 학습하고, 이것을 여러 가지 문제에 적용하여 실제 구현해보는 것을 목표로 한다. 객체지향 프로그래밍은 현재 대다수의 프로그래밍 언어에 채택되고 있는 개념(패러다임)으로, 거의 대부분의 중/대규모 이상의 프로젝트에 적용된다. 이번 강좌에서는 객체지향을 지원하는 여러 프로그래밍 언어(C++, C#, Java, python, ruby 등의 OOP 언어<sup>1</sup>) 중 C++ 중심으로 진행한다.

수업은 크게 아래와 같이 3개 부분으로 진행된다.

1. C/C++ 소개 및 문법
2. 객체지향의 여러 개념(abstraction, encapsulation, polymorphism, inheritance) 및 C++에서의 구현 방법
3. 객체지향 프로그래밍에서 자주 사용되는 디자인 패턴(design pattern)에 대한 소개

[1]: [List of object-oriented programming languages](https://en.wikipedia.org/wiki/List_of_object-oriented_programming_languages)

## 강의 대상

C 혹은 C++ 언어로 프로그래밍한 경험이 있는 것이 도움이 되나, Java, python 등 다른 언어로 프로그래밍 경험이 있으면 처음 3-4주 간은 C/C++ 문법에 대한 리뷰를 진행하므로 수강이 가능하다. 단 기본적인 자료구조(array, list 등), 조건문/반복문(for, while), 함수에 대한 이해와 어떠한 언어로든 이러한 프로그래밍 요소를 사용한 구현 경험이 있어야 한다.

## 수업 방법

수업은 이론 3시간으로 진행되는데, 일부 시간에는 노트북/태블릿 기반으로 일부 실습에 관한 내용을 설명할 수 있다. 일부 실습을 수업 시간에 진행해도 수강하는 학생들은 이론시간에 배우는 C++ 언어의 문법, 객체지향의 개념을 구현하는 방법 등을 과제 혹은 별도의 연습을 하면서 숙지할 필요가 있다. 수업 시간에 일부 코딩을 보여주는 내용이 포함될 수 있다.

개인과제는 학기 중 총 3-4회와 팀 프로젝트로 중규모 프로젝트가 제출될 예정이다.

### 프로젝트

프로젝트는 10월 초에서 중순부터 시작해서, 기말 고사 1-2주 전에 제출하도록 할 예정이다. 프로젝트 주제, 팀, 팀 구성방법 등은 수강하는 학생들의 희망사항을 참고하여, 확정할 예정이다.

현재 계획으로는, 프로젝트는 2-3명의 팀 기반으로 진행하고, 몇 가지 주제 (학생 제안도 좋음) 중에서 선택할 수 있도록 할 예정이다.

## 사용도구

* 개발환경/컴파일러: 이 수업에서는 표준적인 C++(C++ 11 or C++ 14)를 사용할 것이기 때문에, 표준을 지원하는 아래 도구들 중 어떤 것이라도 사용하면 된다
  - [Visual Studio - Microsoft Developer Tools](https://www.visualstudio.com/): [Microsoft](https://www.microsoft.com/ko-kr/)사에서 만든 개발툴. Community 버전은 무료.
  - [Xcode](https://developer.apple.com/xcode/): Mac OS X에 포함되어 있는 개발툴로 C++로 지원
    - 사용방법: - [C++ Development in Xcode](https://jtdaugh.github.io/xcode-umich/)
  - [GCC, the GNU Compiler Collection](https://gcc.gnu.org/) or ["clang" C Language Family Frontend for LLVM](http://clang.llvm.org/): Unix 계열의 OS (Linux, Mac OS X 등)에서 사용가능한 컴파일러
* 온라인 코드실행 및 과제 제출
  - [elice](https://dgist.elice.io/): 코스 과제 제출을 위한 도구로, 웹에서 프로그램을 입력하여 컴파일/실행이 가능하고, 자동채점 기능 제공
* Version control system: 여러 명이 협업할 경우 혹은 혼자 프로젝트를 진행할 경우에도 사용하면 매우 편리함
  - [Git](https://git-scm.com/)
  - [GitHub](https://github.com/)

## 준비물 및 기타

* 개인노트북 (과제/프로젝트 등에 필요) 혹은 태블릿 (노트북 권장)
* 수업시간에 노트북 혹은 태블릿을 가져오면, 노트북에 깔린 개발환경 혹은 웹으로 [elice](https://dgist.elice.io/)에 접속하여 코드를 테스트해 볼 수 있다

## 강의 시간, 교수, 조교
* 교수: 조민규 (mingyu.cho@dgist)
* 조교
  - Jae-Yong Park (darbyyyy@@dgist)
  - Omar Ramirez Sanchez (sanchez@dgist)
* 강의실: E7 242
* 강의시간: 월10:30-12:00, 수9:00-10:30
* Office Hour

| 담당 | Office Hour | 장소 |
|-----|-------------|-----|
| 조민규 | 화 13:30-14:30 | E7 L13 |
| 박재용 | 수 15:30-16:30 | TBD |
| Omar Ramirez Sanchez | 월 13:00-14:00 | TBD |

참고
- Please check the availability of TAs before visiting during office hours.
- If you cannot make any of office hours, send email to arrange a meeting with TAs/faculty.

## 교재

* 권장 (아래 중 하나)
  - Programming: Principles and Practice Using C++, 2nd ed.
  - Jumping into C++
  - Learn C++: http://www.learncpp.com/

* Reference
  - The C++ Programming Language, 4th ed.

* Design patterns (will be covered briefly at the end of class)
  - Design patterns
  - Head first design patterns

## 평가 방법

### 평가 비중 (subject to change)

| 항목   | 비중   |
|----------|----------|
| 중간고사 |  30%     |
| 기말고사 |  30%     |
| 과제 | 20% |
| 프로젝트 | 20% |
| 출석 | ```pow(2, max(n - 3, 0))``` |


### 학점 기준 (subject to change)

| 학점 | 총점 기준 |
|--------|-------------|
| A      | >= 85 |
| B      | >= 70 |
| C      | >= 50 |
| D      | < 50  |
| F      | 출석률, 점수 등 고려 |

## 주차별 계획

| 주차   | 강의계획                                             |
|--------|------------------------------------------------------|
| 1주차  | C/C++ 문법: 컴파일 하는 방법, 변수, 루프, 함수       |
| 2주차  | C/C++ 문법: 포인터, 배열, 함수포인터, struct         |
| 3주차  | C/C++ 문법: 입출력, 메모리 할당                      |
| 4주차  | C/C++ 문법: 클래스, 클래스 할당 (new/delete)         |
| 5주차  | 연산자 오버로딩                                      |
| 6주차  | C++ 표준라이브러리(standard library), 문자열, 스트림 |
| 7주차  | 알고리즘, 이터레이터(iterator), 함수오브젝트         |
| 8주차  | 중간고사                                             |
| 9주차  | 보강 (to be announced)                                 |
| 10주차 | 상속, 다형성                                         |
| 11주차 | 가상함수, 객체지향 설계                              |
| 12주차 | 다중 상속, run-time type identification              |
| 13주차 | 디자인 패턴                                          |
| 14주차 | 디자인 패턴 (con’t)                                  |
| 15주차 | 리뷰                                                 |
| 16주차 | 기말고사                                             |

* 강의 진행에 따라, 일정은 일부 조정될 수 있음

## 참고자료

*책 제목 뒤에 *표시는 한국어 번역본이 있다는 뜻*

* 책
  - [Jumping into C++](https://www.amazon.com/Jumping-into-C-Alex-Allain/dp/0988927802)*: 프로그래밍을 처음 배우는 사람을 대상으로 쉽게 써져 있음
  - [Programming -- Principles and Practice Using C++](http://www.stroustrup.com/programming.html)*: 프로그래밍을 처음 배우는 사람들을 대상으로 C++ 창시자인 [Bjarne Stroustrup](http://www.stroustrup.com/)이 쓴 책. 장점이자 단점은 매우 두껍다
  - [[한빛] 이것이 C++이다: 강의 현장을 그대로 옮긴 C++ 입문서](http://www.hanbit.co.kr/store/books/look.php?p_code=B7010575554):  기본적인 프로그래밍 지식은 있는 사람을 대상으로 쓴 책
  - [Stroustrup: The C++ Programming Language (4th Edition)](http://www.stroustrup.com/4th.html)*: Bjarne Stroustrup이 쓴 책으로 숙련된 프로그래머가 C++를 배울 때 보기 적합한 책. 장점이자 단점은 매우 두껍다
- [Stroustrup: A Tour of C++](http://www.stroustrup.com/Tour.html): Bjarne Stroustrup이 쓴 책으로, 역시 숙력된 프로그래머가 C++의 주요 기능들을 (상대적으로) 빠르게 볼 때 적합한 책
* 디자인 패턴, 객체지향 관련
  - [Design Patterns: Elements of Reusable Object-Oriented Software](https://www.amazon.com/Design-Patterns-Elements-Reusable-Object-Oriented/dp/0201633612): 디자인패턴의 고전으로 저자 혹은 이 책이 Gof(Gang of Four)로 불림 (참고: 번역 수준이 낮다는 평이 있음)
  - [Head First Design Patterns - O'Reilly Media](http://shop.oreilly.com/product/9780596007126.do)*: 디자인 패턴에 대해서 여러 예시와 함께 비교적 평이하게 쓴 책 (예제 코드는 Java를 사용)
  - [객체지향의 사실과 오해](http://wikibook.co.kr/object-orientation/)*: 객체지향으로 프로그램을 설계하는 것을 역할, 책임, 협력관점을 중심으로 기술한 책으로, 객체지향 프로그래밍을 배운 이후에 그 개념을 잡기 좋은 책
* python 프로그래머들을 위한 C/C++ 소개
  - [C for python programmers](http://www.toves.org/books/cpy/)
  - [A Transition Guide: Python to C++](http://dehn.slu.edu/courses/spring08/180/transition.pdf) (24 pages)
* Online Books and tutorial sites on C/C++
  - [C 프로그래밍 입문/C 문법 - 위키책](https://ko.wikibooks.org/wiki/C_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D_%EC%9E%85%EB%AC%B8/C_%EB%AC%B8%EB%B2%95)
  - [C Programming - Wikibooks, open books for an open world](https://en.wikibooks.org/wiki/C_Programming)
  - [How to think like a computer scientist C++ version](http://greenteapress.com/thinkcpp/index.html)
  - [The Rook's Guide to C++](https://rooksguide.files.wordpress.com/2013/12/rooks-guide-isbn-version.pdf)
  - [C++ Programming - Wikibooks, open books for an open world](https://en.wikibooks.org/wiki/C%2B%2B_Programming)
  - [C++ Language - C++ Tutorials](http://www.cplusplus.com/doc/tutorial/)
  - [C++ Tutorial - Learn C++ - Cprogramming.com](http://www.cprogramming.com/tutorial/c++-tutorial.html)
* Miscellaneous
  - [C++ info on stack overflow](http://stackoverflow.com/tags/c++/info)
    - [C++ faq - The Definitive C++ Book Guide and List](http://stackoverflow.com/questions/388242/the-definitive-c-book-guide-and-list)
  - [What are the best C++ books? - Quora](https://www.quora.com/What-are-the-best-C++-books)

## Miscellaneous
- [어떻게 프로그래밍을 공부할 것인가?](https://paper.dropbox.com/doc/UFXkqqqwYBWfpDmigP0WE)
- [이메일 에티켓](https://code.dgist.ac.kr/wiki/이메일-에티켓)
  - 추가: 성적 등 교수만 알아야 될 내용이 아닌 경우, 조교와 교수 모두에게 메일을 보내지 않는 경우 답장을 하지 않을 예정입니다
