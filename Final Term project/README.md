## 2019180041 최현호 기말텀프

### 1. 게임의 소개
**게임의 제목 - 고군분투**
기존에 존재하는 2D 러닝액션 게임으로
게임의 목적은 점프와 와이어 조작을 이용하여 장애물을 통과하면서 많은 점수를 획득하는 게임입니다.
![enter image description here](https://search.pstatic.net/common/?src=http://blogfiles.naver.net/20110802_143/34zz_1312281103981UXXSU_JPEG/%25B0%25ED%25B1%25BA%25BA%25D0%25C5%25F5.jpg&type=sc960_832)
### ↑ 고군분투의 메인 화면![enter image description here](https://search.pstatic.net/common/?src=http://cafefiles.naver.net/MjAyMDA3MThfMjMy/MDAxNTk1MDc3NzUwMDc4.AHk6Gne8mstuW8N-VmgJjZDeoYutMOAGYz4P_8BmjwAg.lARpiPpIzamnU2n1RqtXxvioSFUN0iXNb-u4wZ4Mzu0g.JPEG/%25B0%25ED%25B1%25BA%25BA%25D0%25C5%25F52.jpg&type=sc960_832)
### ↑ 고군분투의 플레이 화면
### 2. Game state
Game state의 수는 3가지로 생각하고 있습니다.
로비 화면을 담당할 **start_state**
게임 방법을 알려줄 화면인 **help_state**
게임 플레이 화면을 담당할 **main_state** 로 구성을 할 계획입니다.

### 3. Game state's detail
**start_state** - 게임의 시작화면
 **게임 시작** 버튼과 **게임 방법** 버튼을 마우스 키를 이용해 누를 수 있도록 만들어 놓을 예정입니다. 각 버튼은 **main_state**와 **help_state**로 전환을 담당할 예정입니다.
 
**help_state** - 게임 방법 설명 화면
**start_state**에서  **게임 방법** 버튼을 눌러서 진입 가능합니다. 게임에 대한 전체적인 설명을 보여줄 예정입니다. **start_state**로 돌아가는 버튼과 **main_state**로 바로 진행하는 버튼을 만들어 볼 예정입니다.

**main_state** - 게임의 진행을 담당할 화면
화면에 표시할 객체에는 **플레이어, 코인(점수), 장애물**이 메인이고, 필요에 따라 다른 객체들이 추가 될 수도 있습니다. 게임오버 상태가 되면
**main_state**를 다시 불러와서 새로 게임을 진행하거나 **start_state**로 돌아갈 수 있는 버튼을 발생할 예정입니다.

### 4. Technique
게임에서 가장 많이 사용될 기술은 아마도 애니메이션이라고 생각합니다. 러닝 게임인 만큼 장애물이 플레이어를 향해 움직이고, 그에 따라 뒤의 배경 역시 움직이기 때문에 이를 해결하는 것이 가장 중요한 요소로 작용할 것이라고 생각합니다.

