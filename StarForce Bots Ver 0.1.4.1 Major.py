import discord
import os
import asyncio
import random

#어빌리티 옵션 목록
 #옵션 첫말
Ab_OpS = ["STR","DEX","INT","LUK","방어력", "최대 HP","최대 MP","점프력","이동속도","공격력",
         "마력","크리티컬확률","모든 능력치","공격속도","AP를 직접 투자한 STR의", "AP를 직접 투자한 DEX의","AP를 직접 투자한 INT의","AP를 직접 투자한 LUK의","일정 레벨마다 공격력 1", "일정 레벨마다 마력 1",
         "방어력","최대 HP","최대 MP","보스몬스터 공격시 데미지","상태이상에 걸린 대상 공격시 데미지", "방어력의","스킬 사용시","패시브 스킬 레벨","다수 공격 스킬의 공격 대상","버프 스킬의 지속시간",
         "아이템 드롭률","메소 획득량","STR","STR","STR ", "DEX ","DEX ","INT ","DEX ","INT ",
         "LUK ","INT ","LUK ","LUK "]
 #옵션 중간말
Ab_OpM = [" "," "," "," "," ", " "," "," "," "," ", " "," "," "," "," ", " "," "," "," "," ", " "," "," "," "," ", " "," "," "," "," ", " "," ","증가 및","증가 및", "증가 및","증가 및","증가 및","증가 및","증가 및", "증가 및","증가 및","증가 및","증가 및","증가 및"]
 #옵션 끝말
Ab_OpE = ["증가","증가","증가","증가","증가", "증가","증가","증가","증가","증가", "증가","% 증가","증가","증가","% 만큼 DEX 증가", "% 만큼 STR 증가","% 만큼 LUK 증가","%만큼 DEX 증가","증가","증가", "% 증가","% 증가","% 증가","% 증가","% 증가", "% 증가","증가","% 확률로 재사용 대기시간이 미적용","증가","증가", "% 증가","% 증가","% 증가",
          "증가","증가","증가","증가","증가","증가","증가","증가","증가","증가","증가","증가"]
 #옵션 설정에 필요한 명성치 (레전-유닉-에픽-레어)
RPT_Cost = [8000,1500,200,100]

 #옵션 설정확률 (레전-유닉-에픽-레어 순 배열)
Ab_Prob = [[400,400,400,400,178, 178,178,0,0,222, 222,44,178,44,222, 222,222,222,222,222, 222,178,178,222,178, 178,178,178,71,71, 89,178,178,311,311, 311,311,311,311,311, 311,311,311,311,311],
           [388,388,388,388,216, 216,216,216,216,129, 129,43,172,0,259, 259,259,259,0,0, 172,172,172,86,172, 172,172,172,0,0, 86,172,172,345,345, 345,345,345,345,345, 345,345,345,345,345],
           [385,385,385,385,299, 257,257,299,257,171, 171,0,257,0,257, 257,257,257,0,0, 0,0,0,0,257, 257,0,0,0,0, 128,257,257,359,359, 359,359,359,359,359, 359,359,359,359,359],
           [351,351,351,351,335, 335,335,335,312,0, 0,0,312,0,234, 234,234,234,0,0, 0,0,0,0,273, 273,0,0,0,0, 312,312,312,351,351, 351,351,351,351,351, 351,351,351,351,351]]
 #옵션 수치 설정확률 (레전-유닉-에픽-레어 순 배열)
Ab_Op_Prob = [] # (개발 예정)

#로얄스타일

Prob_Royal = [310, 300, 320, 320, 250,      150, 350, 300, 500, 150,        350, 300, 400, 500, 500,        500, 500, 500, 500, 500,        500, 500, 500]
Count_Royal = [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0]
Name_Royal = ["[S]푸른 밤 베레모", "[S]푸른 별자리", "[S]푸른 밤 산책", "[S]별빛 연구원(남)/별빛 연구가(여)","[S]푸른 밤 별빛",
              "속죄의 진혼 로브", "속죄의 진혼", "레퀴엠", "속죄의 걸음", "포근 졸려","단잠 리본(남)/낮잠 리본(여)",
              "포근 실내화", "헤어롤", "순수 날개", "마린 티니아 쉐이드", "두근두근쿵쿵",
              "호루라기", "핑크바니 스웨터" , "핑핑하트 스키니", "[30일]포근냥 명찰반지 교환권", "[30일]포근냥 말풍선반지 교환권" , "시원해 냉장고"
              , "스카우터"]

#시드상자

Name_Seed = ["리스트레인트링", "리스크테이커링","웨폰퍼프-S링","웨폰퍼프-D링","웨폰퍼프-L링",
             "웨폰퍼프-I링","얼티메이덤링","링오브 썸 링", "크리데미지링", "레벨퍼프-S링",
             "레벨퍼프-D링","레벨퍼프-L링","레벨퍼프-I링","크라이시스-HM링","듀라빌리티링",
             "크리디펜스링","실드스와프링","헬스컷링","리밋링","오버패스링",
             "버든리프트링","타워인핸스링","크라이시스-H링","크라이시스-M링","리플렉티브링",
             "마나컷링","크리쉬프트링","스탠스쉬프트링","리커버스탠스링","리커버디펜스링",
             "스위프트링","주ㅋ문ㅋ의ㅋ흔ㅋ적ㅋ 180개","주ㅋ문ㅋ의ㅋ흔ㅋ적ㅋ 250개", "시드 포인트 보ㅋ따ㅋ리ㅋ 5개", "의문의 메소주머니",
             "장인의 큐브","류드의 검", "라이트시커", "강력한 환생의 불꽃", "오션 글로우 이어링",
             "깨진 상자조각 3개","깨진 상자조각 4개", "깨진 상자조각 5개"]

Explain_Seed = ["일정 시간동안 일정 영역 내에서 공격력/마력 대폭 상승. 단, 영역을 벗어날 시 상승효과 즉시 해제", "일정 시간동안 공격력/마력 상승. 단, 피격시 상승효과 즉시해제", "일정 시간동안 장착한 주 무기의 기본 공격력/마력에 비례하여 STR스탯 대폭 상승","일정 시간동안 주 무기의 기본 공격력/마력에 비례하여 DEX스탯 대폭 상승","일정 시간동안 장착한 주 무기의 기본 공격력/마력에 비례하여 LUK스탯 대폭 상승",
                "일정 시간동안 장착한 주 무기의 기본 공격력/마력에 비례하여 INT 스탯 대폭 상승", "일정 시간동안 스탯 공격력을 200만으로 고정", "일정 시간동안 모든 스탯의 총합값에 비례하여 자신의 주스탯 대폭 상승", "일정 시간동안 크리티컬 데미지 대폭 상승", "일정 시간동안 캐릭터 레벨에 비례하여 STR 스탯 소폭 상승",
                "일정 시간동안 캐릭터 레벨에 비례하여 DEX 스탯 소폭 상승","일정 시간동안 캐릭터 레벨에 비례하여 LUK 스탯 소폭 상승","일정 시간동안 캐릭터 레벨에 비례하여 INT 스탯 소폭 상승","HP/MP가 모두 5% 미만으로 떨어졌을 때 일정 시간동안 공격력/마력 대폭 상승","일정 시간동안 Max HP가 대폭 상승",
                "일정 시간동안 크리티컬 확률에 비례하여 방어력 무시 증가","일정 시간동안 공격시 방어율 무시 증가. 단, 사용 중 자신의 방어력이 50% 감소","일정 시간동안 보스 공격력 소폭 상승. 단 사용 중 MaxHP가 70% 차감됨","일정 시간동안 보스 공격력 소폭 상승. 단, 사용 중 MaxMP가 500으로 고정됨","일정 시간동안 공격 무효/반사 상태 무시",
                "사용시 높은 확률(80% + 레벨x5%)로 상태이상 해제 및 사용 후 3초간 상태이상 면역","더 시드의 시간제한 맵을 클리어할 경우 일정량의 추가 시드 포인트 지급","자신의 HP가 5% 미만일 경우 일정 시간동안 방어력 소폭 증가","자신의 MP가 5% 미만일 경우 일정 시간동안 방어력 소폭 증가","일정 시간동안 자신이 받는 데미지를 소폭 증폭시켜 반사",
                "일정 시간동안 MaxMP를 70% 낮추고 방어율 소폭 무시","일정 시간동안 크리티컬 확률을 주스탯에 비례한 값으로 대체","일정 시간동안 스탠스 확률을 주스탯에 비례한 값으로 대체","상태이상에 걸린 뒤 회복될 경우 스탠스 확률 증가","상태이상에 걸린 뒤 회복될 경우 상태이상 내성 증가",
                "일정 시간동안 공격속도 2단계 상승","당신의 1시간은 주문의 흔적 180개가 되었습니다.","당신의 1시간은 주문의 흔적 250개가 되었습니다.","꽤 많은(?) 양의 시드 포인트를 주는 보따리이다.","당신의 1시간은 의문의 메소주머니 <1개>가 되었습니다.",
                "당신의 1시간은 장인의 큐브 <1개>가 되었습니다.","이름은...? / 류드...","시드 상자에서 얻을 수 있는 150제 활입니다.","당신의 1시간은 강력한 환생의 불꽃 <1개>가 되었습니다.","시드 상자에서 얻을 수 있는 150제 이어링입니다.",
                "깨진 상자조각 10개를 모아 숨겨진 반지 상자를 얻을 수 있습니다.","깨진 상자조각 10개를 모아 숨겨진 반지 상자를 얻을 수 있습니다.","깨진 상자조각 10개를 모아 숨겨진 반지 상자를 얻을 수 있습니다."]


#팁 목록

Tip = ["Tip) &시드상자 명령어로 2급 시드상자를 시뮬레이션 할 수 있습니다.", "Tip) &매너정보 명령어로 특정 유저의 비매너 전과를 확인할 수 있습니다.", "Tip) &버전확인 명령어로 스타포스 시뮬 봇의 최근 업데이트 내역을 알 수 있습니다.",
       "Tip) 스타포스 시뮬레이션은 MVP로 인한 할인값을 반영하지 않습니다."]

#스타포스 확률표

Prob_Success = [9975, 9450, 8925, 8925, 8400, 7875, 7350, 6825, 6300, 5775, 5250, 4725, 4200, 3675, 3150, 3150, 3150, 3150, 3150, 3150, 3150, 3150] # 성공확률. 예) 9800이면 98%를 의미.
Prob_Break = [0,0,0,0,0, 0,0,0,0,0, 0,0, 58, 127, 137, 206, 206, 206, 274, 274, 685, 685]   # 파괴확률. 예) 67이면 0.67%를 의미.
FallCheck = [0,0,0,0,0,  0,0,0,0,0,  0,1,1,1,1,  0,1,1,1,1,  0,1]  # 0이면 유지, 1이면 등급하락

#슈페리얼 스타포스 확률표

Prob_Superior_Success = [5250, 5250, 4725, 4200, 4200, 4200, 4200, 4200, 4200, 3885, 3675, 3675]
Prob_Superior_Break = [0,0,0,0,0, 180, 300, 420, 600, 950, 1300, 1630]

# 스타포스 가격 (1~22성까지, 각각 130, 140, 150, 160, 200제)

CostData = [[88900, 176800, 264600, 352500, 440400, 528300, 616200, 704000, 791900, 879800, 3561700, 4504600, 5591100, 6829300, 8227500, 19586000, 23069100, 26918600, 31149300, 35776100, 40813400, 46275500],
            [110800, 220500, 330300, 440000, 549800, 659600, 769300, 879100, 988800, 1098600, 4448200, 5625900, 6982900, 8529400, 10275700, 24462200, 28812500, 33620400, 38904500, 44683300, 50974700, 57796700],
            [136000, 271000, 406000, 541000, 676000, 811000, 946000, 1081000, 1216000, 1351000, 5470800, 6919400, 8588400, 10490600, 12638500, 30087200, 35437900, 41351400, 37850600, 54958200, 62696400, 71087200],
            [164800, 328700, 492500, 656400, 820200, 984000, 1147900, 1311700, 1475600, 1639400, 6639400, 8397300, 10422900, 12731500, 15338200, 36514500, 43008300, 50185100, 58072700, 66698700, 76090000, 86273300],
            [321000, 641000, 961000, 1281000, 1601000, 1921000, 2241000, 2561000, 2991000, 3201000, 12966500, 16400100, 20356300, 24865300, 29956500, 71316500, 83999600, 98016700, 113422300, 130270000, 148612400, 168501500]]


#슈페리얼 스타포스 가격

Cost_Heliseum = 5956600
Cost_Nova = 18507900
Cost_Tylent = 55832200

client = discord.Client()
 
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(activity=discord.Game(name="&도움말 for help"))

@client.event
async def on_message(message):

    Main_Channel = client.get_channel(687123978682499083)

    if message.author.id == 345783252361019402: # 박성환 이용 방지
        return
#스타포스 관련 시뮬레이션
 # 파괴방지를 하지 않은 일반 스타포스 시뮬레이션
    async def RGRsimulation(ItemLevel, EventConst, RForceStatus, RForceGoal, UserMoney): # RGRsimulation(렙제, 이벤트, 현재 별, 목표 별, 소지금액). : 파방적용안한 일반 시뮬레이션

        SimulCount = 0 # 시뮬레이션 진행 횟수
        TotalMoney = 0  # 강화 전체 비용
        TotalBreak= 0  # 파괴 횟수
        NonBreak=1000 # 한번도 안 파괴된 경우
        SuccessCount = 0  # 유저가 가진 돈으로 목표에 달성한 횟수
        Event = 0
        ThirtyPer = 0

        if EventConst == 0 : Event = "없음"
        elif EventConst == 1 :
            Event = "스타포스 30% 할인"
            ThirtyPer = 1
        elif EventConst == 2 : Event = "5,10,15성에서 확률 100%"
        elif EventConst == 3 : Event = "10성 이하에서 성공시 1+1"

        # 이벤트값(EventConst) : 0이면 이벤트 없음, 1이면 스타포스 30% 이벤트, 2이면 5,10,15성 100% 이벤트, 3이면 10성 이하에서 1+1 이벤트
        if RForceGoal > 22 :
            if RForceGoal > 25 :await message.channel.send('혹시 메이플스토리가 아닌 다른 게임을 플레이하고 계시나요? 메이플스토리에는 26성 이상의 강화가 없습니다!') 
            else : await message.channel.send('23성 이상 강화라니요... 당신의 장비아이템은 소중합니다. 장비아이템을 소중히 다뤄주세요.')
            return
        elif RForceGoal < 0 :
            await message.channel.send('혹시 메이플스토리가 아닌 다른 게임을 플레이하고 계시나요? 메이플스토리에는 0성 미만의 강화가 없습니다!')
            return
        elif RForceStatus >= RForceGoal :
            await message.channel.send('강화 목표가 현재 강화 상태보다 낮거나 같습니다. 입력이 제대로 되었는지 확인해주세요.')
            return
        elif RForceStatus < 0 :
            await message.channel.send('와우! 음수로 강화된 아이템을 가지고 계시다니! 그런 레어템은 경매장에 올려보는건 어떨까요?')
            return
        if ItemLevel > 200 :
            await message.channel.send('KMS에는 200레벨을 초과하는 강화가능한 아이템이 없습니다. 입력이 제대로 되었는지 확인해주세요.')
            return
        elif ItemLevel < 130 :
            await message.channel.send('해당 레벨대의 아이템 강화에 관한 데이터는 제공하지 않습니다. 양해 부탁드립니다.')
            return
        elif ItemLevel == 130 or ItemLevel == 140 or ItemLevel == 150 or ItemLevel == 160 or ItemLevel == 200 :

            if ItemLevel == 130 :
                itemLevel = 0
                if RForceGoal > 20 :
                    await message.channel.send('130제 아이템은 20성을 초과하는 강화가 불가능합니다.')
                    return
            elif ItemLevel == 140 : itemLevel = 1
            elif ItemLevel == 150 : itemLevel = 2
            elif ItemLevel == 160 : itemLevel = 3
            elif ItemLevel == 200 : itemLevel = 4
            
            while SimulCount < 1000 : # 1000번 시뮬레이션
                UsedMoney = 0  # 1회 시뮬시 총 사용금액
                BreakTimes = 0 # 1회 시뮬시 총 파괴횟수
                IsBroke = 0 # 1회 이상 파괴되었는지 저장할 변수 ( 0 : 파괴X / 1 : 파괴 O )
                Broken12 = 0 # 파괴되었는데 찬스타임이 발동하는 것을 막기 위해
                StatusSaver = [RForceStatus,RForceStatus,RForceStatus]  # 최근 3회의 강화상태를 저장하기 위함
                NowForceStatus = RForceStatus  # 현재 강화상태를 유저의 기본 강화상태로 설정
                
                while NowForceStatus < RForceGoal :  # 강화상태가 목표 강화상태보다 높아지기 전까지 반복

                    UsedMoney = UsedMoney + CostData[itemLevel][NowForceStatus] - 0.3*CostData[itemLevel][NowForceStatus]*ThirtyPer # 파방을 안했다면 그대로. 단, 스타포스 30% 이벤트에는 30% 할인된 금액 적용
                        
                    RandNum = random.randint(0,9999)   # 랜덤함수로 0~9999사이의 난수를 뽑음
     
                    if RandNum < Prob_Success[NowForceStatus] : # 성공시
                        if EventConst == 3 and NowForceStatus <= 10 : NowForceStatus = NowForceStatus + 2  # 1+1 이벤트이고 10성 이하라면 강화단계 2단계 상승
                        else : NowForceStatus = NowForceStatus+1  # 1+1이벤트가 아니거나 1+1이벤이라도 10성 이하가 아니라면 강화단계 1단계 상승
                        
                    elif RandNum < Prob_Success[NowForceStatus] + Prob_Break[NowForceStatus] :  # 파괴시 (파괴가 나는 12성 이상은 1+1이벤 적용 X)
                        if StatusSaver[2] - StatusSaver[0] == 2 and Broken12 < 0 :   # 찬스타임(전전 상태가 현재 상태보다 2단계 높은 상태 == 연속으로 두 등급 떨어진 상황)이라면
                            NowForceStatus = NowForceStatus + 1 # 강화단계 1단계 상승
                                
                        elif EventConst == 2 :  # 찬스타임이 아니고 5,10,15성 100% 이벤이면
                            if NowForceStatus == 15 : NowForceStatus = NowForceStatus + 1 # 15성이라면 100% 이벤에 의해 1단계 상승
                            else : # 어디도 해당사항이 없으면
                                NowForceStatus = 12 # 펑!
                                IsBroke = 1 # 파괴횟수 저장 (한번도 파괴된 적이 없는 경우에서 제외)
                                BreakTimes += 1 # 파괴횟수 + 1
                                Broken12 = 2 # 깨진 템으로 인한 찬스타임을 방지                                
                        else :  # 어디도 해당사항이 없으면
                            NowForceStatus = 12 # 펑!
                            IsBroke = 1 # 파괴횟수 저장 (한번도 파괴된 적이 없는 경우에서 제외)
                            BreakTimes += 1 # 파괴횟수 + 1
                            Broken12 = 2 # 깨진 템으로 인한 찬스타임을 방지
                                
                    else :  # 실패시
                        if StatusSaver[2] - StatusSaver[0] == 2 and Broken12 < 0:   # 찬스타임이면
                            if EventConst == 3 and NowForceStatus <= 10 : NowForceStatus = NowForceStatus + 2 # 1+1이벤에 충족하면 + 2
                            else : NowForceStatus = NowForceStatus + 1 # 아니라면 + 1
                        elif EventConst == 2 : # 찬스타임이 아니고 5,10,15성 이벤트라면
                            if NowForceStatus == 5 or NowForceStatus == 10 or NowForceStatus == 15 : NowForceStatus = NowForceStatus + 1 # 5 10 15성이면 1단계 상승
                            else : NowForceStatus = NowForceStatus - FallCheck[NowForceStatus] # 아니라면 그냥 떨어짐                    
                        else : NowForceStatus = NowForceStatus - FallCheck[NowForceStatus] # 어느 이벤트도 아니라면 그냥 떨어짐

                    Broken12 -= 1 # 깨진 후 최소 2번동안은 찬스타임이 발동하지 않음

                        
                    StatusSaver[2] = StatusSaver[1] # 최근 강화기록 갱신용
                    StatusSaver[1] = StatusSaver[0]
                    StatusSaver[0] = NowForceStatus

                if UsedMoney < UserMoney : SuccessCount += 1 # 유저가 지정한 금액 이하로 썼으면 성공한 횟수++
                TotalMoney += UsedMoney # 평균을 내기 위한 변수 TotalMoney에 이번 시뮬에 쓴 돈을 더해줌.
                SimulCount += 1 # 시뮬레이션한 횟수 추가
                TotalBreak += BreakTimes # 평균을 내기 위한 변수 TotalBreak에 이번 시뮬에서 터진 횟수를 더해줌
                NonBreak -=IsBroke # 만약 한번이라도 파괴되었다면 -1 해줌

            SuccessCount = str(SuccessCount/10)
            TotalBreak = str(TotalBreak/1000)
            TotalMoney = str(TotalMoney/1000)
            NonBreak = str(NonBreak/10)

            embed = discord.Embed(title = "시뮬레이션 결과",description = "스타캐치 전부 성공 가정", color = 0x00FF00)
            embed.add_field(name = "시뮬레이션 대상",value = str(ItemLevel)+"제 아이템", inline = True)
            embed.add_field(name = "시뮬레이션 조건",value = str(RForceStatus)+"->"+str(RForceGoal)+"성", inline = True)
            embed.add_field(name = "파괴방지/이벤트",value = "파괴방지 : X / 이벤트 : "+str(Event),inline = True)
            if UserMoney != -1081599:
                embed.add_field(name = "성공확률", value=SuccessCount + "%", inline=True)
            embed.add_field(name = "평균 파괴횟수",value = TotalBreak,inline = True)
            embed.add_field(name = "1회도 파괴되지 않을 확률", value = NonBreak+"%", inline = True)
            embed.add_field(name = "평균 사용액",value = TotalMoney+"메소",inline = True)
            embed.add_field(name = "경고!", value = "시뮬레이션 결과는 실제와 다를 수 있으니 과신하지 마시기 바랍니다.", inline = False)
            await message.channel.send(message.channel, embed=embed)

        else : await message.channel.send('해당 레벨대의 아이템은 시뮬레이션을 지원하지 않습니다.')
 # 파괴방지를 적용한 스타포스 시뮬레이션
    async def PTsimulation(ItemLevel, EventConst, RForceStatus, RForceGoal, UserMoney): # PTsimulation(렙제, 이벤트, 현재 별, 목표 별, 소지금액). : 파괴방지를 적용한 시뮬레이션

        SimulCount = 0 # 시뮬레이션 진행 횟수
        TotalMoney = 0  # 강화 전체 비용
        TotalBreak= 0  # 파괴 횟수
        NonBreak=1000 # 한번도 안 파괴된 경우
        SuccessCount = 0  # 유저가 가진 돈으로 목표에 달성한 횟수
        Event = 0
        ThirtyPer = 0

        if EventConst == 0 : Event = "없음"
        elif EventConst == 1 :
            Event = "스타포스 30% 할인"
            ThirtyPer = 1
        elif EventConst == 2 : Event = "5,10,15성에서 확률 100%"
        elif EventConst == 3 : Event = "10성 이하에서 성공시 1+1"

        # 이벤트값(EventConst) : 0이면 이벤트 없음, 1이면 스타포스 30% 이벤트, 2이면 5,10,15성 100% 이벤트, 3이면 10성 이하에서 1+1 이벤트
        if RForceGoal > 22 :
            if RForceGoal > 25 :await message.channel.send('혹시 메이플스토리가 아닌 다른 게임을 플레이하고 계시나요? 메이플스토리에는 26성 이상의 강화가 없습니다!') 
            else : await message.channel.send('23성 이상 강화라니요... 당신의 장비아이템은 소중합니다. 장비아이템을 소중히 다뤄주세요.')
            return
        elif RForceGoal < 0 :
            await message.channel.send('혹시 메이플스토리가 아닌 다른 게임을 플레이하고 계시나요? 메이플스토리에는 0성 미만의 강화가 없습니다!')
            return
        elif RForceStatus >= RForceGoal :
            await message.channel.send('강화 목표가 현재 강화 상태보다 낮거나 같습니다. 입력이 제대로 되었는지 확인해주세요.')
            return
        elif RForceStatus < 0 :
            await message.channel.send('와우! 음수로 강화된 아이템을 가지고 계시다니! 그런 레어템은 경매장에 올려보는건 어떨까요?')
            return
        if ItemLevel > 200 :
            await message.channel.send('KMS에는 200레벨을 초과하는 강화가능한 아이템이 없습니다. 입력이 제대로 되었는지 확인해주세요.')
            return
        elif ItemLevel < 130 :
            await message.channel.send('해당 레벨대의 아이템 강화에 관한 데이터는 제공하지 않습니다. 양해 부탁드립니다.')
            return
        elif ItemLevel == 130 or ItemLevel == 140 or ItemLevel == 150 or ItemLevel == 160 or ItemLevel == 200 :

            if ItemLevel == 130 :
                itemLevel = 0
                if RForceGoal > 20 :
                    await message.channel.send('130제 아이템은 20성을 초과하는 강화가 불가능합니다.')
                    return
            elif ItemLevel == 140 : itemLevel = 1
            elif ItemLevel == 150 : itemLevel = 2
            elif ItemLevel == 160 : itemLevel = 3
            elif ItemLevel == 200 : itemLevel = 4
            
            while SimulCount < 1000 : # 1000번 시뮬레이션
                UsedMoney = 0  # 1회 시뮬시 총 사용금액
                BreakTimes = 0 # 1회 시뮬시 총 파괴횟수
                IsBroke = 0 # 1회 이상 파괴되었는지 저장할 변수 ( 0 : 파괴X / 1 : 파괴 O )
                Broken12 = 0 # 파괴되었는데 찬스타임이 발동하는 것을 막기 위해
                StatusSaver = [RForceStatus,RForceStatus,RForceStatus]  # 최근 3회의 강화상태를 저장하기 위함
                NowForceStatus = RForceStatus  # 현재 강화상태를 유저의 기본 강화상태로 설정
                
                while NowForceStatus < RForceGoal :  # 강화상태가 목표 강화상태보다 높아지기 전까지 반복

                    if NowForceStatus >= 12 and NowForceStatus <= 17 and StatusSaver[2] - StatusSaver[0] != 2:  # 만약 파괴방지를 했다면
                        UsedMoney = UsedMoney + 2*CostData[itemLevel][NowForceStatus]   # 파방시에는 드는 돈 2배, 30% 이벤 적용 X
                    else:
                        UsedMoney = UsedMoney + CostData[itemLevel][NowForceStatus] - 0.3*CostData[itemLevel][NowForceStatus]*ThirtyPer # 파방을 안했다면 그대로. 단, 스타포스 30% 이벤트에는 30% 할인된 금액 적용
                        
                    RandNum = random.randint(0,9999)   # 랜덤함수로 0~9999사이의 난수를 뽑음
     
                    if RandNum < Prob_Success[NowForceStatus] : # 성공시
                        if EventConst == 3 and NowForceStatus <= 10 : NowForceStatus = NowForceStatus + 2  # 1+1 이벤트이고 10성 이하라면 강화단계 2단계 상승
                        else : NowForceStatus = NowForceStatus+1  # 1+1이벤트가 아니거나 1+1이벤이라도 10성 이하가 아니라면 강화단계 1단계 상승
                        
                    elif RandNum < Prob_Success[NowForceStatus] + Prob_Break[NowForceStatus] :  # 파괴시 (파괴가 나는 12성 이상은 1+1이벤 적용 X)
                        if StatusSaver[2] - StatusSaver[0] == 2 and Broken12 < 0 :   # 찬스타임(전전 상태가 현재 상태보다 2단계 높은 상태 == 연속으로 두 등급 떨어진 상황)이라면
                            NowForceStatus = NowForceStatus + 1 # 강화단계 1단계 상승
                                
                        elif EventConst == 2 :  # 찬스타임이 아니고 5,10,15성 100% 이벤이면
                            if NowForceStatus == 15 : NowForceStatus = NowForceStatus + 1 # 15성이라면 100% 이벤에 의해 1단계 상승
                            elif NowForceStatus >= 12 and NowForceStatus < 18 : NowForceStatus = NowForceStatus - FallCheck[NowForceStatus] # 파괴방지 적용일 경우 실패로 판정
                            else : # 어디도 해당사항이 없으면
                                NowForceStatus = 12 # 펑!
                                IsBroke = 1 # 파괴횟수 저장 (한번도 파괴된 적이 없는 경우에서 제외)
                                BreakTimes += 1 # 파괴횟수 + 1
                                Broken12 = 2 # 깨진 템으로 인한 찬스타임을 방지
                                
                        else :  # 어디도 해당사항이 없으면
                            if NowForceStatus >= 12 and NowForceStatus < 18 : NowForceStatus = NowForceStatus - FallCheck[NowForceStatus] # 파괴방지 적용일경우 실패로 판정
                            else : # 파괴방지 적용이 아니라면
                                NowForceStatus = 12 # 펑!
                                IsBroke = 1 # 파괴횟수 저장 (한번도 파괴된 적이 없는 경우에서 제외)
                                BreakTimes += 1 # 파괴횟수 + 1
                                Broken12 = 2 # 깨진 템으로 인한 찬스타임을 방지
                                
                    else :  # 실패시
                        if StatusSaver[2] - StatusSaver[0] == 2 and Broken12 < 0:   # 찬스타임이면
                            if EventConst == 3 and NowForceStatus <= 10 : NowForceStatus = NowForceStatus + 2 # 1+1이벤에 충족하면 + 2
                            else : NowForceStatus = NowForceStatus + 1 # 아니라면 + 1
                        elif EventConst == 2 : # 찬스타임이 아니고 5,10,15성 이벤트라면
                            if NowForceStatus == 5 or NowForceStatus == 10 or NowForceStatus == 15 : NowForceStatus = NowForceStatus + 1 # 5 10 15성이면 1단계 상승
                            else : NowForceStatus = NowForceStatus - FallCheck[NowForceStatus] # 아니라면 그냥 떨어짐
                        else : NowForceStatus = NowForceStatus - FallCheck[NowForceStatus] # 어느 이벤트도 아니라면 그냥 떨어짐

                    Broken12 -= 1 # 깨진 후 최소 2번동안은 찬스타임이 발동하지 않음

                        
                    StatusSaver[2] = StatusSaver[1] # 최근 강화기록 갱신용
                    StatusSaver[1] = StatusSaver[0]
                    StatusSaver[0] = NowForceStatus

                if UsedMoney < UserMoney : SuccessCount += 1 # 유저가 지정한 금액 이하로 썼으면 성공한 횟수++
                TotalMoney += UsedMoney # 평균을 내기 위한 변수 TotalMoney에 이번 시뮬에 쓴 돈을 더해줌.
                SimulCount += 1 # 시뮬레이션한 횟수 추가
                TotalBreak += BreakTimes # 평균을 내기 위한 변수 TotalBreak에 이번 시뮬에서 터진 횟수를 더해줌
                NonBreak -=IsBroke # 만약 한번이라도 파괴되었다면 -1 해줌

            SuccessCount = str(SuccessCount/10)
            TotalBreak = str(TotalBreak/1000)
            TotalMoney = str(TotalMoney/1000)
            NonBreak = str(NonBreak/10)

            embed = discord.Embed(title = "시뮬레이션 결과",description = "스타캐치 전부 성공 가정", color = 0x00FF00)
            embed.add_field(name = "시뮬레이션 대상",value = str(ItemLevel)+"제 아이템", inline = True)
            embed.add_field(name = "시뮬레이션 조건",value = str(RForceStatus)+"->"+str(RForceGoal)+"성", inline = True)
            embed.add_field(name = "파괴방지/이벤트",value = "파괴방지 : O / 이벤트 : "+str(Event),inline = True)
            if UserMoney != -1081599:
                embed.add_field(name = "성공확률", value=SuccessCount + "%", inline=True)
            embed.add_field(name = "평균 파괴횟수",value = TotalBreak,inline = True)
            embed.add_field(name = "1회도 파괴되지 않을 확률", value = NonBreak+"%", inline = True)
            embed.add_field(name = "평균 사용액",value = TotalMoney+"메소",inline = True)
            embed.add_field(name = "경고!", value = "시뮬레이션 결과는 실제와 다를 수 있으니 과신하지 마시기 바랍니다.", inline = False)
            await message.channel.send(message.channel, embed=embed)

        else : await message.channel.send('해당 레벨대의 아이템은 시뮬레이션을 지원하지 않습니다.')
 # 슈페리얼 스타포스 시뮬레이션
    async def SUPsimulation(SetName, RForceStatus, RForceGoal, UserMoney):  # SUPsimulation(세트명, 현재 별, 목표 별, 소지금액). : 파방적용안한 일반 시뮬레이션

        ItemCost = 0 # 렙제에 따른 강화비용 저장 함수
        SimulCount = 0  # 시뮬레이션 진행 횟수
        TotalMoney = 0  # 강화 전체 비용
        TotalBreak = 0  # 파괴 횟수
        NonBreak = 1000  # 한번도 안 파괴된 경우
        SuccessCount = 0  # 유저가 가진 돈으로 목표에 달성한 횟수

        if SetName == "헬리시움":
            ItemCost = Cost_Heliseum
        elif SetName == "노바":
            ItemCost = Cost_Nova
        elif SetName == "타일런트":
            ItemCost = Cost_Tylent
        else :
            await message.channel.send('입력하신 세트명이 잘못되었습니다. 다시 입력해주세요.')
            return

        if RForceGoal > 12:
            if RForceGoal > 15:
                await message.channel.send('혹시 슈페리얼 아이템이 아닌 다른 아이템을 강화하고 계시나요? 슈페리얼 아이템은 15성 이상의 강화가 없습니다!')
            else:
                await message.channel.send('12성 이상 강화라니요... 당신의 장비아이템은 소중합니다. 장비아이템을 소중히 다뤄주세요.')
            return
        elif RForceGoal < 0:
            await message.channel.send('혹시 메이플스토리가 아닌 다른 게임을 플레이하고 계시나요? 메이플스토리에는 0성 미만의 강화가 없습니다!')
            return
        elif RForceStatus >= RForceGoal:
            await message.channel.send('강화 목표가 현재 강화 상태보다 낮거나 같습니다. 입력이 제대로 되었는지 확인해주세요.')
            return
        elif RForceStatus < 0:
            await message.channel.send('와우! 음수로 강화된 아이템을 가지고 계시다니! 그런 레어템은 경매장에 올려보는건 어떨까요?')
            return
        if ItemCost == Cost_Heliseum or ItemCost == Cost_Nova or ItemCost == Cost_Tylent:

            if ItemCost == Cost_Heliseum:
                if RForceGoal > 3:
                    await message.channel.send('헬리시움 세트는 3성을 초과하는 강화가 불가능합니다.')
                    return
            elif ItemCost == Cost_Nova:
                if RForceGoal > 10:
                    await message.channel.send('노바 세트는 10성을 초과하는 강화가 불가능합니다.')
                    return

            while SimulCount < 1000:  # 1000번 시뮬레이션
                UsedMoney = 0  # 1회 시뮬시 총 사용금액
                BreakTimes = 0  # 1회 시뮬시 총 파괴횟수
                IsBroke = 0  # 1회 이상 파괴되었는지 저장할 변수 ( 0 : 파괴X / 1 : 파괴 O )
                NowForceStatus = RForceStatus  # 현재 강화상태를 유저의 기본 강화상태로 설정

                while NowForceStatus < RForceGoal:  # 강화상태가 목표 강화상태보다 높아지기 전까지 반복

                    UsedMoney = UsedMoney + ItemCost # 파방을 안했다면 그대로
                    RandNum = random.randint(0, 9999)  # 랜덤함수로 0~9999사이의 난수를 뽑음

                    if RandNum < Prob_Superior_Success[NowForceStatus]:  # 성공시
                        NowForceStatus = NowForceStatus + 1  # 강화단계 1단계 상승
                    elif RandNum < Prob_Superior_Success[NowForceStatus] + Prob_Superior_Break[NowForceStatus]: # 파괴시
                        NowForceStatus = 0  # 펑!
                        IsBroke = 1  # 파괴횟수 저장 (한번도 파괴된 적이 없는 경우에서 제외)
                        BreakTimes += 1  # 파괴횟수 + 1
                    else:  # 실패시
                        if NowForceStatus == 0:
                            NowForceStatus = 0 # 강화단계 1단계 하락
                        else : NowForceStatus = NowForceStatus - 1

                if UsedMoney < UserMoney: SuccessCount += 1  # 유저가 지정한 금액 이하로 썼으면 성공한 횟수++
                TotalMoney += UsedMoney  # 평균을 내기 위한 변수 TotalMoney에 이번 시뮬에 쓴 돈을 더해줌.
                SimulCount += 1  # 시뮬레이션한 횟수 추가
                TotalBreak += BreakTimes  # 평균을 내기 위한 변수 TotalBreak에 이번 시뮬에서 터진 횟수를 더해줌
                NonBreak -= IsBroke  # 만약 한번이라도 파괴되었다면 -1 해줌

            SuccessCount = str(SuccessCount / 10)
            TotalBreak = str(TotalBreak / 1000)
            TotalMoney = str(TotalMoney / 1000)
            NonBreak = str(NonBreak / 10)

            embed = discord.Embed(title="시뮬레이션 결과", description="스타캐치 전부 성공 가정", color=0x00FF00)
            embed.add_field(name="시뮬레이션 대상", value=SetName + " 세트 아이템", inline=True)
            embed.add_field(name="시뮬레이션 조건", value=str(RForceStatus) + "->" + str(RForceGoal) + "성", inline=True)
            if UserMoney != -1081599:
                embed.add_field(name="성공확률", value=SuccessCount + "%", inline=True)
            embed.add_field(name="평균 파괴횟수", value=TotalBreak, inline=True)
            embed.add_field(name="1회도 파괴되지 않을 확률", value=NonBreak + "%", inline=True)
            embed.add_field(name="평균 사용액", value=TotalMoney + "메소", inline=True)
            embed.add_field(name="경고!", value="시뮬레이션 결과는 실제와 다를 수 있으니 과신하지 마시기 바랍니다.", inline=False)
            await message.channel.send(message.channel, embed=embed)
 # 도움말
    if message.content.startswith('&도움말'):
        print('User request : help')
        await Main_Channel.send('User Request : help')
        embed = discord.Embed(title = "도움말",description ="제작자의 군 입대로 인하여 2020.06.08 ~ 2021.12.07 사이의 기간동안 추가적 패치를 진행할 수 없습니다. 이와 관련된 부분에 대해선 &공지사항 명령어를 통해 확인해주세요."  ,color=0x00FF00)
        embed.add_field(name = "&스타포스", value = "스타포스 시뮬레이션과 관련된 도움말을 출력합니다. (기능이 너무 많아 별도 설명란으로 옮겼습니다.)", inline = False)
        embed.add_field(name = "&로얄 (사용할 개수)", value = "현재 판매중인 로얄스타일을 시뮬레이션 합니다. 시뮬레이션 개수는 100만개를 초과할 수 없습니다.", inline = False)
        embed.add_field(name = "&시드상자", value = "2급 시드상자 1개를 개봉하는 시뮬레이션을 진행합니다. 단, 모든 아이템의 확률이 동일하다 가정합니다.",inline = False)
        embed.add_field(name = "&레시피 (아이템명)", value = "(베타 버전입니다.) 해당 아이템의 제작 레시피와 관련된 정보를 출력합니다.",inline = False)
        embed.add_field(name = "&보스정보 (보스명)", value = "해당 보스몬스터의 정보를 출력합니다. 띄어쓰기 없이 사용해야 합니다. (예시 : 이지 자쿰을 검색한다면 [&보스정보 이지자쿰]과 같이 입력.")
        embed.add_field(name = "&버전확인", value = "현재 스타포스 시뮬레이션 봇의 버전과 최근 업데이트 내역을 확인합니다.",inline = False)
        embed.add_field(name = "문의사항", value = "문의사항이나 오류발견/건의는 다음 URL로 해주시기 바랍니다. : https://www.blueappleteam.ml/64",inline = False)
        embed.add_field(name = "봇 초대 URL", value = "https://discordapp.com/oauth2/authorize?client_id=673972036485382168&permissions=67584&scope=bot", inline = False)
        await message.channel.send(message.channel, embed=embed)
 # 스타포스 시뮬 관련 도움말
    elif message.content.startswith('&스타포스'):
        print('User request : help')
        await Main_Channel.send('User Request : starforce help')
        embed = discord.Embed(title="도움말",description ="이 봇에서는 스타캐치를 모두 성공하는 것으로 가정하였으며, 스타캐치로 상승하는 확률은 3%로 가정하였습니다."  ,color=0x00FF00)
        embed.add_field(name = "&시뮬 (아이템 레벨) (현재 강화차수) (목표 강화차수)", value = "해당 레벨과 강화차수의 아이템을 목표 강화차수까지 1000번 시뮬레이션한 결과를 보여줍니다.", inline = False)
        embed.add_field(name = "&이벤시뮬 (이벤트명) (아이템 레벨) (현재 강화차수) (목표 강화차수)", value = "이벤트를 적용하여 시뮬레이션을 진행합니다. 단, [30% 이벤트 : 30%], [5,10,15성 100% 이벤트 : 100%], [10성 이하 1+1 이벤트 : 1+1]으로 입력해야합니다.", inline = False)
        embed.add_field(name = "&파방시뮬 (아이템 레벨) (현재 강화차수) (목표 강화차수)", value = "파괴방지를 적용하여 시뮬레이션을 진행합니다. 단, 도중에 파괴방지를 해제하지 않습니다.", inline = False)
        embed.add_field(name = "&이벤파방시뮬 (이벤트명) (아이템 레벨) (현재 강화차수) (목표 강화차수)",value = "이벤트와 파괴방지를 적용하여 시뮬레이션을 진행합니다. 5,10,15성 100% 이벤트의 경우 15성에서는 파괴방지 가격을 적용하지 않습니다.", inline = False)
        embed.add_field(name = "&성공확률 (아이템 레벨) (현재 강화차수) (목표 강화차수) (소지금액)",value = "해당 레벨과 강화차수의 아이템을 목표 강화차수까지 1000번 시뮬레이션하여 소지금액 내로 성공할 확률을 계산하여 보여줍니다.", inline = False)
        embed.add_field(name = "&이벤성공확률 (이벤트명) (아이템 레벨) (현재 강화차수) (목표 강화차수) (소지금액)", value = "이벤트를 적용하여 소지금액 내로 성공할 확률을 계산하여 보여줍니다. 단, [30% 이벤트 : 30%], [5,10,15성 100% 이벤트 : 100%], [10성 이하 1+1 이벤트 : 1+1]으로 입력해야 합니다.", inline = False)
        embed.add_field(name = "&파방성공확률 (아이템 레벨) (현재 강화차수) (목표 강화차수) (소지금액)",value = "파괴방지를 적용하여 소지금액 내로 성공할 확률을 계산하여 보여줍니다. 단, 도중에 파괴방지를 해제하지 않습니다.", inline = False)
        embed.add_field(name = "&이벤파방성공확률 (이벤트명) (아이템 레벨) (현재 강화차수) (목표 강화차수) (소지금액)", value = "이벤트와 파괴방지를 적용하여 시뮬레이션을 진행합니다. 5,10,15성 100% 이벤트의 경우 15성에서는 파괴방지 가격을 적용하지 않습니다.", inline = False)
        embed.add_field(name = "&슈페리얼 (세트명) (현재 강화차수) (목표 강화차수)",value="해당 슈페리얼 세트와 강화차수의 아이템을 목표 강화차수까지 1000번 시뮬레이션한 결과를 보여줍니다.", inline=False)
        embed.add_field(name = "&슈페리얼성공확률 (세트명) (현재 강화차수) (목표 강화차수) (소지금액)",value="해당 슈페리얼 세트와 강화차수의 아이템을 목표 강화차수까지 1000번 시뮬레이션하여 소지금액 내로 성공할 확률을 계산하여 보여줍니다.", inline=False)
        await message.channel.send(message.channel, embed=embed)
 # 스타포스 시뮬 명령어
    elif message.content.startswith('&시뮬'):
        InputData = message.content.split(" ")
        embed = discord.Embed(title = "Simulation Request",description = "Request has been received",color = 0x00FF00)
        embed.add_field(name = "Author", value = str(message.author.name), inline = True)
        embed.add_field(name = "Server", value = str(message.guild.name), inline = True)
        embed.add_field(name = "Channel", value = str(message.channel.name), inline = True)
        try : embed.add_field(name = "Contents", value = InputData[0] + " " + InputData[1] +" "+InputData[2]+" "+InputData[3], inline = True)
        except :
            await message.channel.send('입력하신 명령어가 잘못되었습니다. 다시 시도해주세요.')
            await Main_Channel.send('Bad Request, Request completed')
        await Main_Channel.send(embed=embed)
        await RGRsimulation(int(InputData[1]), 0, int(InputData[2]), int(InputData[3]), -1081599)
        print('Request completed')
    elif message.content.startswith('&이벤시뮬'):
        InputData = message.content.split(" ")
        embed = discord.Embed(title = "Simulation Request",description = "Request has been received",color = 0x00FF00)
        embed.add_field(name = "Author", value = str(message.author.name), inline = True)
        embed.add_field(name = "Server", value = str(message.guild.name), inline = True)
        embed.add_field(name = "Channel", value = str(message.channel.name), inline = True)
        try : embed.add_field(name = "Contents", value = InputData[0] + " " + InputData[1] +" "+InputData[2]+" "+InputData[3]+" "+InputData[4], inline = True)
        except :
            await message.channel.send('입력하신 명령어가 잘못되었습니다. 다시 시도해주세요.')
            await Main_Channel.send('Bad Request, Request completed')
        await Main_Channel.send(embed=embed)
        if InputData[1] == "30%":
            await RGRsimulation(int(InputData[2]), 1, int(InputData[3]), int(InputData[4]), -1081599)
        elif InputData[1] == "100%":
            await RGRsimulation(int(InputData[2]), 2, int(InputData[3]), int(InputData[4]), -1081599)
        elif InputData[1] == "1+1":
            await RGRsimulation(int(InputData[2]), 3, int(InputData[3]), int(InputData[4]), -1081599)
        else :
            print('Bad Request : EventConst Error')
            await message.channel.send('이벤트명을 잘못 입력하셨습니다. 다시 시도해주세요.')
            await Main_Channel.send('Bad Request, Request Completed')
        print('Request completed')
    elif message.content.startswith('&파방시뮬'):
        InputData = message.content.split(" ")
        embed = discord.Embed(title = "Simulation Request",description = "Request has been received",color = 0x00FF00)
        embed.add_field(name = "Author", value = str(message.author.name), inline = True)
        embed.add_field(name = "Server", value = str(message.guild.name), inline = True)
        embed.add_field(name = "Channel", value = str(message.channel.name), inline = True)
        try : embed.add_field(name = "Contents", value = InputData[0] + " " + InputData[1] +" "+InputData[2]+" "+InputData[3], inline = True)
        except :
            await message.channel.send('입력하신 명령어가 잘못되었습니다. 다시 시도해주세요.')
            await Main_Channel.send('Bad Request, Request completed')
        await Main_Channel.send(embed=embed)
        await PTsimulation(int(InputData[1]),0, int(InputData[2]),int(InputData[3]),-1081599)
        print('Request completed')
    elif message.content.startswith('&이벤파방시뮬'):
        InputData = message.content.split(" ")
        embed = discord.Embed(title = "Simulation Request",description = "Request has been received",color = 0x00FF00)
        embed.add_field(name = "Author", value = str(message.author.name), inline = True)
        embed.add_field(name = "Server", value = str(message.guild.name), inline = True)
        embed.add_field(name = "Channel", value = str(message.channel.name), inline = True)
        try : embed.add_field(name = "Contents", value = InputData[0] + " " + InputData[1] +" "+InputData[2]+" "+InputData[3]+" "+InputData[4], inline = True)
        except :
            await message.channel.send('입력하신 명령어가 잘못되었습니다. 다시 시도해주세요.')
            await Main_Channel.send('Bad Request, Request completed')
        await Main_Channel.send(embed=embed)
        if InputData[1] == "30%":
            await PTsimulation(int(InputData[2]), 1, int(InputData[3]), int(InputData[4]), -1081599)
        elif InputData[1] == "100%":
            await PTsimulation(int(InputData[2]), 2, int(InputData[3]), int(InputData[4]), -1081599)
        elif InputData[1] == "1+1":
            await PTsimulation(int(InputData[2]), 3, int(InputData[3]), int(InputData[4]), -1081599)
        else :
            print('Bad Request : EventConst Error')
            await message.channel.send('이벤트명을 잘못 입력하셨습니다. 다시 시도해주세요.')
            await Main_Channel.send('Bad Request, Request Completed')
        print('Request completed')
    elif message.content.startswith('&성공확률'):
        InputData = message.content.split(" ")
        embed = discord.Embed(title = "Simulation Request",description = "Request has been received",color = 0x00FF00)
        embed.add_field(name = "Author", value = str(message.author.name), inline = True)
        embed.add_field(name = "Server", value = str(message.guild.name), inline = True)
        embed.add_field(name = "Channel", value = str(message.channel.name), inline = True)
        try : embed.add_field(name = "Contents", value = InputData[0] + " " + InputData[1] +" "+InputData[2]+" "+InputData[3]+" "+InputData[4], inline = True)
        except :
            await message.channel.send('입력하신 명령어가 잘못되었습니다. 다시 시도해주세요.')
            await Main_Channel.send('Bad Request, Request completed')
        await Main_Channel.send(embed=embed)
        await RGRsimulation(int(InputData[1]), 0, int(InputData[2]), int(InputData[3]), int(InputData[4]))
        print('Request completed')
    elif message.content.startswith('&이벤성공확률'):
        InputData = message.content.split(" ")
        embed = discord.Embed(title = "Simulation Request",description = "Request has been received",color = 0x00FF00)
        embed.add_field(name = "Author", value = str(message.author.name), inline = True)
        embed.add_field(name = "Server", value = str(message.guild.name), inline = True)
        embed.add_field(name = "Channel", value = str(message.channel.name), inline = True)
        try : embed.add_field(name = "Contents", value = InputData[0] + " " + InputData[1] +" "+InputData[2]+" "+InputData[3]+" "+InputData[4]+" "+InputData[5], inline = True)
        except :
            await message.channel.send('입력하신 명령어가 잘못되었습니다. 다시 시도해주세요.')
            await Main_Channel.send('Bad Request, Request completed')
        await Main_Channel.send(embed=embed)
        if InputData[1] == "30%":
            await RGRsimulation(int(InputData[2]), 1, int(InputData[3]), int(InputData[4]), int(InputData[5]))
        elif InputData[1] == "100%":
            await RGRsimulation(int(InputData[2]), 2, int(InputData[3]), int(InputData[4]), int(InputData[5]))
        elif InputData[1] == "1+1":
            await RGRsimulation(int(InputData[2]), 3, int(InputData[3]), int(InputData[4]), int(InputData[5]))
        else :
            print('Bad Request : EventConst Error')
            await message.channel.send('이벤트명을 잘못 입력하셨습니다. 다시 시도해주세요.')
            await Main_Channel.send('Bad Request, Request Completed')
        print('Request completed')
    elif message.content.startswith('&파방성공확률'):
        InputData = message.content.split(" ")
        embed = discord.Embed(title = "Simulation Request",description = "Request has been received",color = 0x00FF00)
        embed.add_field(name = "Author", value = str(message.author.name), inline = True)
        embed.add_field(name = "Server", value = str(message.guild.name), inline = True)
        embed.add_field(name = "Channel", value = str(message.channel.name), inline = True)
        try : embed.add_field(name = "Contents", value = InputData[0] + " " + InputData[1] +" "+InputData[2]+" "+InputData[3]+" "+InputData[4], inline = True)
        except :
            await message.channel.send('입력하신 명령어가 잘못되었습니다. 다시 시도해주세요.')
            await Main_Channel.send('Bad Request, Request completed')
        await Main_Channel.send(embed=embed)
        await PTsimulation(int(InputData[1]),0,int(InputData[2]),int(InputData[3]),int(InputData[4]))
        print('Request completed')
    elif message.content.startswith('&이벤파방성공확률'):
        InputData = message.content.split(" ")
        embed = discord.Embed(title = "Simulation Request",description = "Request has been received",color = 0x00FF00)
        embed.add_field(name = "Author", value = str(message.author.name), inline = True)
        embed.add_field(name = "Server", value = str(message.guild.name), inline = True)
        embed.add_field(name = "Channel", value = str(message.channel.name), inline = True)
        try : embed.add_field(name = "Contents", value = InputData[0] + " " + InputData[1] +" "+InputData[2]+" "+InputData[3]+" "+InputData[4]+" "+InputData[5], inline = True)
        except :
            await message.channel.send('입력하신 명령어가 잘못되었습니다. 다시 시도해주세요.')
            await Main_Channel.send('Bad Request, Request completed')
        await Main_Channel.send(embed=embed)
        if InputData[1] == "30%":
            await PTsimulation(int(InputData[2]), 1, int(InputData[3]), int(InputData[4]), int(InputData[5]))
        elif InputData[1] == "100%":
            await PTsimulation(int(InputData[2]), 2, int(InputData[3]), int(InputData[4]), int(InputData[5]))
        elif InputData[1] == "1+1":
            await PTsimulation(int(InputData[2]), 3, int(InputData[3]), int(InputData[4]), int(InputData[5]))
        else :
            print('Bad Request : EventConst Error')
            await message.channel.send('이벤트명을 잘못 입력하셨습니다. 다시 시도해주세요.')
            await Main_Channel.send('Bad Request, Request Completed')
        print('Request completed')
    elif message.content.startswith('&슈페리얼성공확률'):
        InputData = message.content.split(" ")
        embed = discord.Embed(title="Simulation Request", description="Request has been received", color=0x00FF00)
        embed.add_field(name="Author", value=str(message.author.name), inline=True)
        embed.add_field(name="Server", value=str(message.guild.name), inline=True)
        embed.add_field(name="Channel", value=str(message.channel.name), inline=True)
        try: embed.add_field(name="Contents", value=InputData[0] + " " + InputData[1] + " " + InputData[2] + " " + InputData[3] + " " + InputData[4], inline=True)
        except:
            await message.channel.send('입력하신 명령어가 잘못되었습니다. 다시 시도해주세요.')
            await Main_Channel.send('Bad Request, Request completed')
        await Main_Channel.send(embed=embed)
        await SUPsimulation(InputData[1], int(InputData[2]), int(InputData[3]), int(InputData[4]))
        print('Request completed')
    elif message.content.startswith('&슈페리얼'):
        InputData = message.content.split(" ")
        embed = discord.Embed(title="Simulation Request", description="Request has been received", color=0x00FF00)
        embed.add_field(name="Author", value=str(message.author.name), inline=True)
        embed.add_field(name="Server", value=str(message.guild.name), inline=True)
        embed.add_field(name="Channel", value=str(message.channel.name), inline=True)
        try: embed.add_field(name="Contents", value=InputData[0] + " " + InputData[1] + " " + InputData[2] + " " + InputData[3], inline=True)
        except:
            await message.channel.send('입력하신 명령어가 잘못되었습니다. 다시 시도해주세요.')
            await Main_Channel.send('Bad Request, Request completed')
        await Main_Channel.send(embed=embed)

        await SUPsimulation(InputData[1], int(InputData[2]), int(InputData[3]), -1081599)
        print('Request completed')

#어빌리티 관련 시뮬레이션
  # 명성치 시뮬레이션 (개발예정)
  # 서큘 시뮬레이션 (개발예정)

#로얄스타일
    elif message.content.startswith('&로얄') :
        InputData = message.content.split(" ")         
        embed = discord.Embed(title = "Royal Request",description = "Request has been received",color = 0x00FF00)
        embed.add_field(name = "Author", value = str(message.author.name), inline = True)
        embed.add_field(name = "Server", value = str(message.guild.name), inline = True)
        embed.add_field(name = "Channel", value = str(message.channel.name), inline = True)
        embed.add_field(name = "Contents", value = InputData[0] + " " + InputData[1], inline = True)
        await Main_Channel.send(embed=embed)        
        try : InputData[1] = int(InputData[1])
        except :
            await message.channel.send('입력하신 로얄스타일의 개수가 자연수가 아닙니다. 다시 시도해주세요.')
            print('Request completed')
            await Main_Channel.send('Bad Request, Request completed')
        if int(InputData[1]) > 10000 :
            await message.channel.send('로얄스타일 시뮬레이션은 최대 1만번까지만 시행할 수 있습니다. 다시 시도해주세요.')
            print('Request completed')
            await Main_Channel.send('Bad Request, Request completed')            
        elif int(InputData[1]) < 1 :
            await message.channel.send('최소 1개 이상의 값을 입력해주시기 바랍니다. 다시 시도해주세요.')
            print('Request completed')
            await Main_Channel.send('Bad Request, Request completed')            
        
        else :
            for RoyalCounter in range(0, 23, 1) :
                Count_Royal[RoyalCounter] = 0
            for RoyalCounter in range (0, int(InputData[1]), 1) :
                RandNum = random.randint(0,9999)   # 랜덤함수로 0~9999사이의 난수를 뽑음
                for RoyalNum in range (1, 24, 1) :
                    TotalProb = 0
                    for Prob in range (0, RoyalNum, 1) : TotalProb += Prob_Royal[Prob]
                    if RandNum < TotalProb :
                        Count_Royal[RoyalNum-1] += 1
                        break
            embed = discord.Embed(title = "로얄 결과",description = "사용한 로얄 갯수 : "+str(InputData[1])+"개", color = 0x00FF00)
            for RoyalShow in range (0, 23, 1) :
                if Count_Royal[RoyalShow] != 0 :
                    embed.add_field(name = str(Name_Royal[RoyalShow]),value = str(Count_Royal[RoyalShow])+"개", inline = True)
            embed.add_field(name = "경고!", value = "시뮬레이션 결과는 실제와 다를 수 있으니 과신하지 마시기 바랍니다.", inline = False)
            embed.add_field(name = "공지사항", value = "봇 개발자의 군 입대로 인하여 2021년 7월 6일이 마지막 갱신일임에 유의해주시기 바랍니다.", inline = False)
            await message.channel.send(message.channel, embed=embed)
            await Main_Channel.send(embed=embed)            
            print('Request completed')
#시드 상자
    elif message.content.startswith('&시드상자') :      
        embed = discord.Embed(title = "Seed Request",description = "Request has been received",color = 0x00FF00)
        embed.add_field(name = "Author", value = str(message.author.name), inline = True)
        embed.add_field(name = "Server", value = str(message.guild.name), inline = True)
        embed.add_field(name = "Channel", value = str(message.channel.name), inline = True)
        await Main_Channel.send(embed=embed)

        RandNum = random.randint(0,42) # 랜덤함수로 0~42 사이의 난수를 뽑음

        if RandNum < 31 :
            RingLevel = random.randint(1,4) #랜덤함수로 1~4 사이의 난수를 뽑음
            embed = discord.Embed(title = "시드 상자 개봉 결과",description = "2급 시드상자를 개봉한 결과 다음과 같은 아이템이 나왔습니다!", color = 0x00FF00)
            embed.add_field(name = Name_Seed[RandNum]+ " "+str(RingLevel)+"레벨", value = Explain_Seed[RandNum], inline = False)
            embed.add_field(name = "경고!", value = "시뮬레이션 결과는 실제와 다를 수 있으니 과신하지 마시기 바랍니다.", inline = False)
            await message.channel.send(message.channel, embed=embed)
            embed = discord.Embed(title = "Request completed",description = "Request has been completed",color = 0x00FF00)
            embed.add_field(name = "Result", value = Name_Seed[RandNum]+ " "+str(RingLevel)+"레벨", inline = True)       
            await Main_Channel.send(embed=embed)
        
        else :
            embed = discord.Embed(title = "시드 상자 개봉 결과",description = "2급 시드상자를 개봉한 결과 다음과 같은 아이템이 나왔습니다!", color = 0x00FF00)
            embed.add_field(name = Name_Seed[RandNum], value = Explain_Seed[RandNum], inline = False)
            embed.add_field(name = "경고!", value = "시뮬레이션 결과는 실제와 다를 수 있으니 과신하지 마시기 바랍니다.", inline = False)
            await message.channel.send(message.channel, embed=embed)
            embed = discord.Embed(title = "Request completed",description = "Request has been completed",color = 0x00FF00)
            embed.add_field(name = "Result", value = Name_Seed[RandNum], inline = True)       
            await Main_Channel.send(embed=embed)
#레시피
    elif message.content.startswith('&레시피') :
        InputData = message.content.split(" ")            
        embed = discord.Embed(title = "Recipe Request",description = "Request has been received",color = 0x00FF00)
        embed.add_field(name = "Author", value = str(message.author.name), inline = True)
        embed.add_field(name = "Server", value = str(message.guild.name), inline = True)
        embed.add_field(name = "Channel", value = str(message.channel.name), inline = True)
        embed.add_field(name = "Contents", value = InputData[0] + " " + InputData[1], inline = True)
        await Main_Channel.send(embed=embed)

        if InputData[1] == "재획비" or InputData[1] == "재물획득의비약" :
            embed = discord.Embed(title = "재물 획득의 비약",description = "권장 연금술 레벨 : 10 / 사용가능 레벨 : 70",color = 0x00FF00)
            embed.add_field(name = "재료", value = "최고급 포션 빈 병 x1 / 쥬니퍼베리 씨앗 오일 x10 / 최상급 아이템 결정 x3 / 현자의 돌 x1", inline = True)
            embed.add_field(name = "제작 쿨타임", value = "5분", inline = True)
            embed.add_field(name = "1회 제작시 획득량", value = "3개", inline = True)
            await message.channel.send(message.channel, embed=embed)
        elif InputData[1] == "경축비" or InputData[1] == "경험축적의비약" :
            embed = discord.Embed(title = "경험 축적의 비약",description = "권장 연금술 레벨 : 10 / 사용가능 레벨 : 70",color = 0x00FF00)
            embed.add_field(name = "재료", value = "최고급 포션 빈 병 x1 / 쥬니퍼베리 씨앗 오일 x10 / 최상급 아이템 결정 x5 / 현자의 돌 x2", inline = True)
            embed.add_field(name = "제작 쿨타임", value = "5분", inline = True)
            embed.add_field(name = "1회 제작시 획득량", value = "3개", inline = True)
            await message.channel.send(message.channel, embed=embed)
        else : await message.channel.send('존재하지 않는 레시피거나 해당 아이템이 서버에 기록되어 있지 않습니다. 띄어쓰기를 사용하지 않고 입력해주세요. \n예시 : 경험 축적의 비약에 관한 정보를 얻고 싶다면 [&레시피 경험축적의비약] 입력')
#보스정보
    elif message.content.startswith('&보스정보') or message.content.startswith('&보스') :
        InputData = message.content.split(" ")
        embed = discord.Embed(title = "BossData Request",description = "Request has been received",color = 0x00FF00)
        embed.add_field(name = "Author", value = str(message.author.name), inline = True)
        embed.add_field(name = "Server", value = str(message.guild.name), inline = True)
        embed.add_field(name = "Channel", value = str(message.channel.name), inline = True)
        embed.add_field(name = "Contents", value = message.content, inline = True)
        await Main_Channel.send(embed=embed)

        # 띄어쓰기 방지구문
        if InputData[1] == "이지" or InputData[1] == "노말" or InputData[1] == "하드" or InputData[1] == "카오스" or InputData[1] == "노멀" :
            await message.channel.send('난이도를 제외한 보스 이름만을 입력하거나 보스이름을 띄어쓰기 하지 않고 입력해주세요. \n예시 : 노말 윌에 관한 정보를 얻고 싶다면 [&보스정보 윌] 혹은 [&보스정보 노말윌] 입력')
            return

        # 마왕 발록
        elif InputData[1] == "발록" or InputData[1] == "마왕" or InputData[1] == "마왕발록" or InputData[1] == "이지발록" or InputData[1] == "이지마왕발록" :
            embed = discord.Embed(title = "보스몬스터 [마왕 발록] 정보",description = "보스몬스터 [마왕 발록]의 정보를 제공해드립니다.",color = 0x0000FF)
            embed.add_field(name = "입장 요구레벨", value = "Lv.65", inline = True)
            embed.add_field(name = "몬스터 레벨", value = "Lv.60", inline = True)
            embed.add_field(name = "제한시간", value = "20분", inline = True)
            embed.add_field(name = "데스카운트", value = "없음" , inline = True)
            embed.add_field(name = "물약 쿨타임", value = "없음", inline = True)
            embed.add_field(name = "페이즈 개수", value = "2개 (구분되지 않음)", inline = False)
            embed.add_field(name = "1페이즈 체력", value = "알 수 없음 (데미지가 들어가지 않음)", inline = False)
            embed.add_field(name = "2페이즈 체력", value = "4,787,520 (478만 7520)", inline = False)
            embed.add_field(name = "방어율", value = "25%", inline = True)
            embed.add_field(name = "파티격 요구스펙", value = "60레벨 이상", inline = False)
            embed.add_field(name = "솔격 요구스펙", value = "60레벨 이상", inline = False)
            embed.add_field(name = "결정석 가격", value = "결정석을 드랍하지 않음", inline = False)
            embed.add_field(name = "확정 드랍 보상", value = "발록의 가죽조각", inline = False)
            embed.add_field(name = "확률적 드랍 보상", value = "발록의 무기/방어구, 발록의 소울조각, 발록 라이딩", inline = False)
            embed.add_field(name = "공략 영상 URL", value = "(추후 영상 첨부)", inline = False)
            embed.add_field(name = "패턴 정보", value = "https://namu.wiki/w/마왕%20발록#s-4", inline = False)
            embed.set_thumbnail(url = "https://ww.namu.la/s/ec3e7a0adfa03afcd7906e8baf7e45bae8fb7b88030cfc664d31afe1d9e6c7ffb711fbff5039bdd6eeb9f9a0c772a6a2269d259320104a176e38fd415c1aad071154ba90afa7d0328262ea19f6d33cb25efb2ccd56594c227ebc1c70a69d70d6")
            await message.channel.send(message.channel, embed=embed)           

        # 자쿰
        elif InputData[1] == "자쿰" :
            await message.channel.send('이지/노말/카오스 자쿰에 대한 정보를 출력합니다.')
            await message.channel.send('&보스정보 이지자쿰')
            await message.channel.send('&보스정보 노말자쿰')
            await message.channel.send('&보스정보 카오스자쿰')
            return
        elif InputData[1] == "이지자쿰" :
            embed = discord.Embed(title = "보스몬스터 [이지 자쿰] 정보",description = "보스몬스터 [이지 자쿰]의 정보를 제공해드립니다.",color = 0x0000FF)
            embed.add_field(name = "입장 요구레벨", value = "Lv.50", inline = True)
            embed.add_field(name = "몬스터 레벨", value = "Lv.50", inline = True)
            embed.add_field(name = "제한시간", value = "20분", inline = True)
            embed.add_field(name = "데스카운트", value = "50개" , inline = True)
            embed.add_field(name = "물약 쿨타임", value = "10초", inline = True)
            embed.add_field(name = "페이즈 개수", value = "3개 (구분되지 않음, 일부 페이즈 스킵가능)", inline = False)
            embed.add_field(name = "본체 체력", value = "2,200,000 (220만)", inline = False)
            embed.add_field(name = "팔 총합 체력", value = "1,632,000 (163만 2000)", inline = False)
            embed.add_field(name = "방어율", value = "30%", inline = True)
            embed.add_field(name = "파티격 요구스펙", value = "50레벨 이상", inline = False)
            embed.add_field(name = "솔격 요구스펙", value = "50레벨 이상", inline = False)
            embed.add_field(name = "결정석 가격", value = "[본섭] 20만 메소 \n[리부트] 60만 메소", inline = False)
            embed.add_field(name = "확정 드랍 보상", value = "없음 (십자코인 등 기초아이템은 존재)", inline = False)
            embed.add_field(name = "확률적 드랍 보상", value = "자쿰의 투구", inline = False)
            embed.add_field(name = "공략 영상 URL", value = "(추후 영상 첨부)", inline = False)
            embed.add_field(name = "패턴 정보", value = "https://namu.wiki/w/자쿰(메이플스토리)#s-4", inline = False)
            embed.set_thumbnail(url = "https://ww.namu.la/s/c1f2c962039400c56031de42b64ecbf64eee95542994b5e39a0e9e5aa3c282bbf40867d40f2226734ac9357d55fe343149eee69d990b81a63cb910a051287ea34bb02dd98beefbb050176084e6b5362e391a25450bb85ed40372cbc8cfeb0b95")
            await message.channel.send(message.channel, embed=embed)
        elif InputData[1] == "노말자쿰" or InputData[1] == "노멀자쿰":
            embed = discord.Embed(title = "보스몬스터 [노말 자쿰] 정보",description = "보스몬스터 [노말 자쿰]의 정보를 제공해드립니다.",color = 0x0000FF)
            embed.add_field(name = "입장 요구레벨", value = "Lv.90", inline = True)
            embed.add_field(name = "몬스터 레벨", value = "Lv.110", inline = True)
            embed.add_field(name = "제한시간", value = "30분", inline = True)
            embed.add_field(name = "데스카운트", value = "5개" , inline = True)
            embed.add_field(name = "물약 쿨타임", value = "10초", inline = True)
            embed.add_field(name = "페이즈 개수", value = "3개 (구분되지 않음, 일부 페이즈 스킵가능)", inline = False)
            embed.add_field(name = "본체 체력", value = "7,000,000 (700만)", inline = False)
            embed.add_field(name = "팔 총합 체력", value = "5,600,000 (560만)", inline = False)
            embed.add_field(name = "방어율", value = "40%", inline = True)
            embed.add_field(name = "파티격 요구스펙", value = "100레벨 이상", inline = False)
            embed.add_field(name = "솔격 요구스펙", value = "100레벨 이상", inline = False)
            embed.add_field(name = "결정석 가격", value = "[본섭] 61만 2500메소 \n[리부트] 183만 7500메소", inline = False)
            embed.add_field(name = "확정 드랍 보상", value = "자쿰의 투구", inline = False)
            embed.add_field(name = "확률적 드랍 보상", value = "응축된 힘의 결정석, 아쿠아틱 레더 눈장식, 자쿰의 포이즈닉 무기, 자쿰의 소울조각", inline = False)
            embed.add_field(name = "공략 영상 URL", value = "(추후 영상 첨부)", inline = False)
            embed.add_field(name = "패턴 정보", value = "https://namu.wiki/w/자쿰(메이플스토리)#s-4", inline = False)
            embed.set_thumbnail(url = "https://ww.namu.la/s/c1f2c962039400c56031de42b64ecbf64eee95542994b5e39a0e9e5aa3c282bbf40867d40f2226734ac9357d55fe343149eee69d990b81a63cb910a051287ea34bb02dd98beefbb050176084e6b5362e391a25450bb85ed40372cbc8cfeb0b95")
            await message.channel.send(message.channel, embed=embed)
        elif InputData[1] == "카오스자쿰" or InputData[1] == "카쿰" :
            embed = discord.Embed(title = "보스몬스터 [카오스 자쿰] 정보",description = "보스몬스터 [카오스 자쿰]의 정보를 제공해드립니다.",color = 0x0000FF)
            embed.add_field(name = "입장 요구레벨", value = "Lv.90", inline = True)
            embed.add_field(name = "몬스터 레벨", value = "Lv.180", inline = True)
            embed.add_field(name = "제한시간", value = "30분", inline = True)
            embed.add_field(name = "데스카운트", value = "5개" , inline = True)
            embed.add_field(name = "물약 쿨타임", value = "10초", inline = True)
            embed.add_field(name = "페이즈 개수", value = "3개 (구분되지 않음, 일부 페이즈 스킵가능)", inline = False)
            embed.add_field(name = "본체 체력", value = "84,000,000,000 (840억)", inline = False)
            embed.add_field(name = "팔 총합 체력", value = "84,000,000,000 (840억)", inline = False)
            embed.add_field(name = "방어율", value = "100%", inline = True)
            embed.add_field(name = "파티격 요구스펙", value = "180레벨 이상, 무릉 30층 이상", inline = False)
            embed.add_field(name = "솔격 요구스펙", value = "180레벨 이상, 무릉 34층 이상", inline = False)
            embed.add_field(name = "결정석 가격", value = "[본섭] 1620만 메소 \n[리부트] 4860만 메소", inline = False)
            embed.add_field(name = "확정 드랍 보상", value = "카오스 자쿰의 투구, 카오스 자쿰의 나뭇가지", inline = False)
            embed.add_field(name = "확률적 드랍 보상", value = "응축된 힘의 결정석, 아쿠아틱 레더 눈장식, 자쿰의 포이즈닉 무기, 분노한 자쿰 장비, 자쿰의 소울조각", inline = False)
            embed.add_field(name = "공략 영상 URL", value = "(추후 영상 첨부)", inline = False)
            embed.add_field(name = "패턴 정보", value = "https://namu.wiki/w/자쿰(메이플스토리)#s-4", inline = False)
            embed.set_thumbnail(url = "https://ww.namu.la/s/c1f2c962039400c56031de42b64ecbf64eee95542994b5e39a0e9e5aa3c282bbf40867d40f2226734ac9357d55fe343149eee69d990b81a63cb910a051287ea34bb02dd98beefbb050176084e6b5362e391a25450bb85ed40372cbc8cfeb0b95")
            await message.channel.send(message.channel, embed=embed) 

        # 파풀라투스
        # 파풀라투스
        elif InputData[1] == "파풀라투스" :
            await message.channel.send('이지/노말/카오스 파풀라투스에 대한 정보를 출력합니다.')
            await message.channel.send('&보스정보 이지파풀라투스')
            await message.channel.send('&보스정보 노말파풀라투스')
            await message.channel.send('&보스정보 카오스파풀라투스')
            return
        elif InputData[1] == "이지파풀라투스" :
            embed = discord.Embed(title = "보스몬스터 [이지 파풀라투스] 정보",description = "보스몬스터 [이지 파풀라투스]의 정보를 제공해드립니다.",color = 0x0000FF)
            embed.add_field(name = "입장 요구레벨", value = "Lv.115", inline = True)
            embed.add_field(name = "몬스터 레벨", value = "Lv.125", inline = True)
            embed.add_field(name = "제한시간", value = "30분", inline = True)
            embed.add_field(name = "데스카운트", value = "50개" , inline = True)
            embed.add_field(name = "물약 쿨타임", value = "없음 (시계알람때 5초)", inline = True)
            embed.add_field(name = "페이즈 개수", value = "2개", inline = False)
            embed.add_field(name = "1페이즈 체력", value = "300,000,000 (3억)", inline = False)
            embed.add_field(name = "2페이즈 체력", value = "100,000,000 (1억)", inline = False)
            embed.add_field(name = "방어율", value = "50%", inline = True)
            embed.add_field(name = "파티격 요구스펙", value = "115레벨 이상", inline = False)
            embed.add_field(name = "솔격 요구스펙", value = "115레벨 이상", inline = False)
            embed.add_field(name = "결정석 가격", value = "[본섭] 68만 4500메소 \n[리부트] 205만 3500메소", inline = False)
            embed.add_field(name = "확정 드랍 보상", value = "없음 (십자코인 등 기초아이템은 존재)", inline = False)
            embed.add_field(name = "확률적 드랍 보상", value = "없음", inline = False)
            embed.add_field(name = "공략 영상 URL", value = "(추후 영상 첨부)", inline = False)
            embed.add_field(name = "패턴 정보", value = "https://namu.wiki/w/파풀라투스#s-4", inline = False)
            embed.set_thumbnail(url = "https://w.namu.la/s/e2802bf19462e4cefb4b7c3e32a7feb95deda730a54960c7114ed18783fc8e4757755df1deec15596f276f17d3165eeba1496300327d37a2bd43f33d9a9da0f5fc15f7fb767c3bf24148c988a8ea6f4104d699ba69ce7dfc9a7ff8c0ad56f1fb")
            await message.channel.send(message.channel, embed=embed)
        elif InputData[1] == "노말파풀라투스" or InputData[1] == "노멀파풀라투스" :
            embed = discord.Embed(title = "보스몬스터 [노말 파풀라투스] 정보",description = "보스몬스터 [노말 파풀라투스]의 정보를 제공해드립니다.",color = 0x0000FF)
            embed.add_field(name = "입장 요구레벨", value = "Lv.155", inline = True)
            embed.add_field(name = "몬스터 레벨", value = "Lv.155", inline = True)
            embed.add_field(name = "제한시간", value = "30분", inline = True)
            embed.add_field(name = "데스카운트", value = "5개" , inline = True)
            embed.add_field(name = "물약 쿨타임", value = "없음 (시계알람때 5초)", inline = True)
            embed.add_field(name = "페이즈 개수", value = "2개", inline = False)
            embed.add_field(name = "1페이즈 체력", value = "12,450,000,000 (124억 5천만)", inline = False)
            embed.add_field(name = "2페이즈 체력", value = "4,150,000,000 (41억 5천만)", inline = False)
            embed.add_field(name = "방어율", value = "50%", inline = True)
            embed.add_field(name = "파티격 요구스펙", value = "155레벨 이상, 무릉 20층 이상", inline = False)
            embed.add_field(name = "솔격 요구스펙", value = "155레벨 이상, 무릉 20층 이상", inline = False)
            embed.add_field(name = "결정석 가격", value = "[본섭] 266만 4500메소 \n[리부트] 799만 3500메소", inline = False)
            embed.add_field(name = "확정 드랍 보상", value = "없음 (십자코인 등 기초아이템은 존재)", inline = False)
            embed.add_field(name = "확률적 드랍 보상", value = "파풀라투스 시계의자, 파풀라투스의 소울조각", inline = False)
            embed.add_field(name = "공략 영상 URL", value = "(추후 영상 첨부)", inline = False)
            embed.add_field(name = "패턴 정보", value = "https://namu.wiki/w/파풀라투스#s-4", inline = False)
            embed.set_thumbnail(url = "https://w.namu.la/s/e2802bf19462e4cefb4b7c3e32a7feb95deda730a54960c7114ed18783fc8e4757755df1deec15596f276f17d3165eeba1496300327d37a2bd43f33d9a9da0f5fc15f7fb767c3bf24148c988a8ea6f4104d699ba69ce7dfc9a7ff8c0ad56f1fb")
            await message.channel.send(message.channel, embed=embed)
        elif InputData[1] == "카오스파풀라투스" or InputData[1] == "카파풀" :
            embed = discord.Embed(title = "보스몬스터 [카오스 파풀라투스] 정보",description = "보스몬스터 [카오스 파풀라투스]의 정보를 제공해드립니다.",color = 0x0000FF)
            embed.add_field(name = "입장 요구레벨", value = "Lv.190", inline = True)
            embed.add_field(name = "몬스터 레벨", value = "Lv.190", inline = True)
            embed.add_field(name = "제한시간", value = "30분", inline = True)
            embed.add_field(name = "데스카운트", value = "5개" , inline = True)
            embed.add_field(name = "물약 쿨타임", value = "없음 (시계알람때 5초)", inline = True)
            embed.add_field(name = "페이즈 개수", value = "2개", inline = False)
            embed.add_field(name = "1페이즈 체력", value = "378,000,000,000 (3780억)", inline = False)
            embed.add_field(name = "2페이즈 체력", value = "126,000,000,000 (1260억)", inline = False)
            embed.add_field(name = "전체 체력", value = "504,000,000,000 (5040억)", inline = False)
            embed.add_field(name = "방어율", value = "250%", inline = True)
            embed.add_field(name = "파티격 요구스펙", value = "무릉 40층 이상", inline = False)
            embed.add_field(name = "솔격 요구스펙", value = "[비숍 / 배틀메이지] 무릉 37층 이상 \n[타 직업] 무릉 41층 이상", inline = False)
            embed.add_field(name = "결정석 가격", value = "[본섭] 2645만 메소 \n[리부트] 7935만 메소", inline = False)
            embed.add_field(name = "확정 드랍 보상", value = "없음 (십자코인 등 기초아이템은 존재)", inline = False)
            embed.add_field(name = "확률적 드랍 보상", value = "파풀라투스 시계의자, 파풀라투스 마크, 파풀라투스의 소울조각", inline = False)
            embed.add_field(name = "공략 영상 URL", value = "(추후 영상 첨부)", inline = False)
            embed.add_field(name = "패턴 정보", value = "https://namu.wiki/w/파풀라투스#s-4", inline = False)
            embed.set_thumbnail(url = "https://w.namu.la/s/e2802bf19462e4cefb4b7c3e32a7feb95deda730a54960c7114ed18783fc8e4757755df1deec15596f276f17d3165eeba1496300327d37a2bd43f33d9a9da0f5fc15f7fb767c3bf24148c988a8ea6f4104d699ba69ce7dfc9a7ff8c0ad56f1fb")
            await message.channel.send(message.channel, embed=embed)
        # 매그너스
        elif InputData[1] == "매그너스" :
            await message.channel.send('이지/노말/하드 매그너스에 대한 정보를 출력합니다.')
            await message.channel.send('&보스정보 이지매그너스')
            await message.channel.send('&보스정보 노말매그너스')
            await message.channel.send('&보스정보 하드매그너스')
            return
        elif InputData[1] == "이지매그너스" :
            embed = discord.Embed(title = "보스몬스터 [이지 매그너스] 정보",description = "보스몬스터 [이지 매그너스]의 정보를 제공해드립니다.",color = 0x0000FF)
            embed.add_field(name = "입장 요구레벨", value = "Lv.115", inline = True)
            embed.add_field(name = "몬스터 레벨", value = "Lv.110", inline = True)
            embed.add_field(name = "제한시간", value = "30분", inline = True)
            embed.add_field(name = "데스카운트", value = "5개" , inline = True)
            embed.add_field(name = "물약 쿨타임", value = "5초", inline = True)
            embed.add_field(name = "페이즈 개수", value = "3개 (구분되지 않음)", inline = False)
            embed.add_field(name = "전체 체력", value = "4,000,000 (400만)", inline = False)
            embed.add_field(name = "방어율", value = "50%", inline = True)
            embed.add_field(name = "파티격 요구스펙", value = "스공 5만 이상", inline = False)
            embed.add_field(name = "솔격 요구스펙", value = "스공 5만 이상", inline = False)
            embed.add_field(name = "결정석 가격", value = "[본섭] 72만 2000메소 \n[리부트] 216만 6000메소", inline = False)
            embed.add_field(name = "확정 드랍 보상", value = "그림자 상인단 코인", inline = False)
            embed.add_field(name = "확률적 드랍 보상", value = "크리스탈 웬투스 뱃지, 로얄 블랙메탈 숄더, 노바 방어구", inline = False)
            embed.add_field(name = "공략 영상 URL", value = "(추후 영상 첨부)", inline = False)
            embed.add_field(name = "패턴 정보", value = "https://namu.wiki/w/매그너스(메이플스토리)/보스%20몬스터#s-4", inline = False)
            embed.set_thumbnail(url = "https://w.namu.la/s/767fdcbfb8754974694817d5f82fefd41296a7b1994a0e945bd6599732250271e2f03509e190f4f6c10509767ffbbb988f522e951c3ffb067cc0a484a8354f24fed858ec1ec93b99452134487d7464737b37d266b59dd37e19d2bfae60b9d2db")
            await message.channel.send(message.channel, embed=embed)
        elif InputData[1] == "노말매그너스" or InputData[1] == "노멀매그너스" :
            embed = discord.Embed(title = "보스몬스터 [노말 매그너스] 정보",description = "보스몬스터 [노말 매그너스]의 정보를 제공해드립니다.",color = 0x0000FF)
            embed.add_field(name = "입장 요구레벨", value = "Lv.155", inline = True)
            embed.add_field(name = "몬스터 레벨", value = "Lv.130", inline = True)
            embed.add_field(name = "제한시간", value = "30분", inline = True)
            embed.add_field(name = "데스카운트", value = "10개" , inline = True)
            embed.add_field(name = "물약 쿨타임", value = "5초", inline = True)
            embed.add_field(name = "페이즈 개수", value = "4개 (구분되지 않음)", inline = False)
            embed.add_field(name = "전체 체력", value = "6,000,000,000 (60억)", inline = False)
            embed.add_field(name = "방어율", value = "50%", inline = True)
            embed.add_field(name = "파티격 요구스펙", value = "155레벨 이상 및 스공 20만 이상", inline = False)
            embed.add_field(name = "솔격 요구스펙", value = "무릉 20층 이상", inline = False)
            embed.add_field(name = "결정석 가격", value = "[본섭] 259만 2000메소 \n[리부트] 777만 6000메소", inline = False)
            embed.add_field(name = "확정 드랍 보상", value = "그림자 상인단 코인", inline = False)
            embed.add_field(name = "확률적 드랍 보상", value = "크리스탈 웬투스 뱃지, 로얄 블랙메탈 숄더, 노바 방어구, 매그너스의 소울조각", inline = False)
            embed.add_field(name = "공략 영상 URL", value = "(추후 영상 첨부)", inline = False)
            embed.add_field(name = "패턴 정보", value = "https://namu.wiki/w/매그너스(메이플스토리)/보스%20몬스터#s-4", inline = False)
            embed.set_thumbnail(url = "https://w.namu.la/s/767fdcbfb8754974694817d5f82fefd41296a7b1994a0e945bd6599732250271e2f03509e190f4f6c10509767ffbbb988f522e951c3ffb067cc0a484a8354f24fed858ec1ec93b99452134487d7464737b37d266b59dd37e19d2bfae60b9d2db")
            await message.channel.send(message.channel, embed=embed)
        elif InputData[1] == "하드매그너스" or InputData[1] == "하매" :
            embed = discord.Embed(title = "보스몬스터 [하드 매그너스] 정보",description = "보스몬스터 [하드 매그너스]의 정보를 제공해드립니다.",color = 0x0000FF)
            embed.add_field(name = "입장 요구레벨", value = "Lv.175", inline = True)
            embed.add_field(name = "몬스터 레벨", value = "Lv.190", inline = True)
            embed.add_field(name = "제한시간", value = "30분", inline = True)
            embed.add_field(name = "데스카운트", value = "15개" , inline = True)
            embed.add_field(name = "물약 쿨타임", value = "5초", inline = True)
            embed.add_field(name = "페이즈 개수", value = "4개 (구분되지 않음)", inline = False)
            embed.add_field(name = "전체 체력", value = "120,000,000,000 (1200억)", inline = False)
            embed.add_field(name = "방어율", value = "120%", inline = True)
            embed.add_field(name = "파티격 요구스펙", value = "무릉 34층 이상", inline = False)
            embed.add_field(name = "솔격 요구스펙", value = "무릉 37층 이상", inline = False)
            embed.add_field(name = "결정석 가격", value = "[본섭] 1901만 2500메소 \n[리부트] 5703만 6000메소", inline = False)
            embed.add_field(name = "확정 드랍 보상", value = "매그너스 코인", inline = False)
            embed.add_field(name = "확률적 드랍 보상", value = "크리스탈 웬투스 뱃지, 로얄 블랙메탈 숄더, 노바 방어구, 타일런트 망토, 저주받은 카이세리움, 매그너스의 소울조각", inline = False)
            embed.add_field(name = "공략 영상 URL", value = "(추후 영상 첨부)", inline = False)
            embed.add_field(name = "패턴 정보", value = "https://namu.wiki/w/매그너스(메이플스토리)/보스%20몬스터#s-4", inline = False)
            embed.set_thumbnail(url = "https://w.namu.la/s/767fdcbfb8754974694817d5f82fefd41296a7b1994a0e945bd6599732250271e2f03509e190f4f6c10509767ffbbb988f522e951c3ffb067cc0a484a8354f24fed858ec1ec93b99452134487d7464737b37d266b59dd37e19d2bfae60b9d2db")
            await message.channel.send(message.channel, embed=embed)
        # 힐라
        elif InputData[1] == "힐라" :
            await message.channel.send('노말 힐라와 하드 힐라에 대한 정보를 출력합니다.')
            await message.channel.send('&보스정보 노말힐라')
            await message.channel.send('&보스정보 하드힐라')
        elif InputData[1] == "노말힐라" or InputData[1] == "노멀힐라" :
            embed = discord.Embed(title = "보스몬스터 [노말 힐라] 정보",description = "보스몬스터 [노말 힐라]의 정보를 제공해드립니다.",color = 0x0000FF)
            embed.add_field(name = "입장 요구레벨", value = "Lv.125", inline = True)
            embed.add_field(name = "몬스터 레벨", value = "Lv.110", inline = True)
            embed.add_field(name = "제한시간", value = "30분", inline = True)
            embed.add_field(name = "데스카운트", value = "무한" , inline = True)
            embed.add_field(name = "물약 쿨타임", value = "없음", inline = True)
            embed.add_field(name = "페이즈 개수", value = "1개", inline = False)
            embed.add_field(name = "전체 체력", value = "500,000,000 (5억)", inline = False)
            embed.add_field(name = "방어율", value = "50%", inline = True)
            embed.add_field(name = "파티격 요구스펙", value = "120레벨 이상", inline = False)
            embed.add_field(name = "솔격 요구스펙", value = "120레벨 이상", inline = False)
            embed.add_field(name = "결정석 가격", value = "[본섭] 80만 메소 \n[리부트] 240만 메소", inline = False)
            embed.add_field(name = "확정 드랍 보상", value = "없음 (십자코인 등 기초아이템은 존재)", inline = False)
            embed.add_field(name = "확률적 드랍 보상", value = "영생의 돌, 다크소울의 펫상자, 네크로 세트 장비아이템, 힐라의 소울조각", inline = False)
            embed.add_field(name = "공략 영상 URL", value = "(추후 영상 첨부)", inline = False)
            embed.add_field(name = "패턴 정보", value = "https://namu.wiki/w/힐라/보스%20몬스터#s-3", inline = False)
            embed.set_thumbnail(url = "https://w.namu.la/s/ce192667d7351bb01ad50a2db28703fcfb3c3835092ac58096062027a28f9c82c9a42fc9b7e16cc0a28d69a350813856fd7c6659288088a73c7dc4463e2d313dbcb471ab691496d3405820ec5fdec8c7a24f89e4f05928104d9ff31f0d19831d")
            await message.channel.send(message.channel, embed=embed)
        elif InputData[1] == "하드힐라" or InputData[1] == "하힐" :
            embed = discord.Embed(title = "보스몬스터 [하드 힐라] 정보",description = "보스몬스터 [하드 힐라]의 정보를 제공해드립니다.",color = 0x0000FF)
            embed.add_field(name = "입장 요구레벨", value = "Lv.170", inline = True)
            embed.add_field(name = "몬스터 레벨", value = "Lv.190", inline = True)
            embed.add_field(name = "제한시간", value = "30분", inline = True)
            embed.add_field(name = "데스카운트", value = "15개" , inline = True)
            embed.add_field(name = "물약 쿨타임", value = "없음", inline = True)
            embed.add_field(name = "페이즈 개수", value = "2개 (구분되지 않음)", inline = False)
            embed.add_field(name = "전체 체력", value = "16,800,000,000 (168억)", inline = False)
            embed.add_field(name = "방어율", value = "100%", inline = True)
            embed.add_field(name = "파티격 요구스펙", value = "무릉 29층 이상", inline = False)
            embed.add_field(name = "솔격 요구스펙", value = "무릉 29층 이상", inline = False)
            embed.add_field(name = "결정석 가격", value = "[본섭] 1125만 메소 \n[리부트] 3375만 메소", inline = False)
            embed.add_field(name = "확정 드랍 보상", value = "없음 (십자코인 등 기초아이템은 존재)", inline = False)
            embed.add_field(name = "확률적 드랍 보상", value = "영생의 돌, 다크소울의 펫상자, 네크로 세트 장비아이템, 지옥의 불꽃, 힐라의 소울조각", inline = False)
            embed.add_field(name = "공략 영상 URL", value = "(추후 영상 첨부)", inline = False)
            embed.add_field(name = "패턴 정보", value = "https://namu.wiki/w/힐라/보스%20몬스터#s-3", inline = False)
            embed.set_thumbnail(url = "https://w.namu.la/s/ce192667d7351bb01ad50a2db28703fcfb3c3835092ac58096062027a28f9c82c9a42fc9b7e16cc0a28d69a350813856fd7c6659288088a73c7dc4463e2d313dbcb471ab691496d3405820ec5fdec8c7a24f89e4f05928104d9ff31f0d19831d")
            await message.channel.send(message.channel, embed=embed)
        # 혼테일
        elif InputData[1] == "혼테일" :
            await message.channel.send('이지/노말/카오스 혼테일에 대한 정보를 출력합니다.')
            await message.channel.send('&보스정보 이지혼테일')
            await message.channel.send('&보스정보 노말혼테일')
            await message.channel.send('&보스정보 카오스혼테일')
            return
        elif InputData[1] == "이지혼테일" :
            embed = discord.Embed(title = "보스몬스터 [이지 혼테일] 정보",description = "보스몬스터 [이지 혼테일]의 정보를 제공해드립니다.",color = 0x0000FF)
            embed.add_field(name = "입장 요구레벨", value = "Lv.130", inline = True)
            embed.add_field(name = "몬스터 레벨", value = "Lv.130", inline = True)
            embed.add_field(name = "제한시간", value = "1시간 15분", inline = True)
            embed.add_field(name = "데스카운트", value = "10개" , inline = True)
            embed.add_field(name = "물약 쿨타임", value = "없음", inline = True)
            embed.add_field(name = "페이즈 개수", value = "3개", inline = False)
            embed.add_field(name = "1페이즈 체력", value = "100,000,000 (1억)", inline = False)
            embed.add_field(name = "2페이즈 체력", value = "100,000,000 (1억)", inline = False)
            embed.add_field(name = "3페이즈 체력", value = "817,600,600  (8억 1760만)", inline = False)
            embed.add_field(name = "전체 체력", value = "1,017,600,000 (10억 1760만)", inline = False)
            embed.add_field(name = "방어율", value = "타격위치에 따라 달라짐", inline = True)
            embed.add_field(name = "파티격 요구스펙", value = "130레벨 이상", inline = False)
            embed.add_field(name = "솔격 요구스펙", value = "130레벨 이상", inline = False)
            embed.add_field(name = "결정석 가격", value = "[본섭] 88만 2000메소 \n[리부트] 264만 6000메소", inline = False)
            embed.add_field(name = "확정 드랍 보상", value = "없음 (십자코인 등 기초아이템은 존재)", inline = False)
            embed.add_field(name = "확률적 드랍 보상", value = "실버블라썸 링, 데아 시두스 이어링", inline = False)
            embed.add_field(name = "공략 영상 URL", value = "(추후 영상 첨부)", inline = False)
            embed.add_field(name = "패턴 정보", value = "https://namu.wiki/w/혼테일#s-5", inline = False)
            embed.set_thumbnail(url = "https://ww.namu.la/s/897a6c291fd033e8afc661c8b944c0e1cfab12c4be04add3676d17bc4d61379b199b4086a1596f48b245b252131e3a510105bc9b9387cfb7a7075c7963e0d08122a98578647e000040321a7ce5c32eedb8d05250194fd095ff5de96e1c697b3f")
            await message.channel.send(message.channel, embed=embed)
        elif InputData[1] == "노말혼테일" or InputData[1] == "노멀혼테일" :
            embed = discord.Embed(title = "보스몬스터 [노말 혼테일] 정보",description = "보스몬스터 [노말 혼테일]의 정보를 제공해드립니다.",color = 0x0000FF)
            embed.add_field(name = "입장 요구레벨", value = "Lv.130", inline = True)
            embed.add_field(name = "몬스터 레벨", value = "Lv.160", inline = True)
            embed.add_field(name = "제한시간", value = "1시간 15분", inline = True)
            embed.add_field(name = "데스카운트", value = "10개" , inline = True)
            embed.add_field(name = "물약 쿨타임", value = "없음", inline = True)
            embed.add_field(name = "페이즈 개수", value = "3개", inline = False)
            embed.add_field(name = "1페이즈 체력", value = "330,000,000 (3억 3천만)", inline = False)
            embed.add_field(name = "2페이즈 체력", value = "330,000,000 (3억 3천만)", inline = False)
            embed.add_field(name = "3페이즈 체력", value = "2,090,000,000 (20억 9천만)", inline = False)
            embed.add_field(name = "전체 체력", value = "2,750,000,000 (27억 5천만)", inline = False)
            embed.add_field(name = "방어율", value = "타격위치에 따라 달라짐", inline = True)
            embed.add_field(name = "파티격 요구스펙", value = "160레벨 이상", inline = False)
            embed.add_field(name = "솔격 요구스펙", value = "180레벨 이상", inline = False)
            embed.add_field(name = "결정석 가격", value = "[본섭] 101만 2500메소 \n[리부트] 303만 7500메소", inline = False)
            embed.add_field(name = "확정 드랍 보상", value = "없음 (십자코인 등 기초아이템은 존재)", inline = False)
            embed.add_field(name = "확률적 드랍 보상", value = "실버블라썸 링, 데아 시두스 이어링, 혼테일의 목걸이", inline = False)
            embed.add_field(name = "공략 영상 URL", value = "(추후 영상 첨부)", inline = False)
            embed.add_field(name = "패턴 정보", value = "https://namu.wiki/w/혼테일#s-5", inline = False)
            embed.set_thumbnail(url = "https://ww.namu.la/s/897a6c291fd033e8afc661c8b944c0e1cfab12c4be04add3676d17bc4d61379b199b4086a1596f48b245b252131e3a510105bc9b9387cfb7a7075c7963e0d08122a98578647e000040321a7ce5c32eedb8d05250194fd095ff5de96e1c697b3f")
            await message.channel.send(message.channel, embed=embed)
        elif InputData[1] == "카오스혼테일" or InputData[1] == "카혼" :
            embed = discord.Embed(title = "보스몬스터 [카오스 혼테일] 정보",description = "보스몬스터 [카오스 혼테일]의 정보를 제공해드립니다.",color = 0x0000FF)
            embed.add_field(name = "입장 요구레벨", value = "Lv.135", inline = True)
            embed.add_field(name = "몬스터 레벨", value = "Lv.160", inline = True)
            embed.add_field(name = "제한시간", value = "2시간 30분", inline = True)
            embed.add_field(name = "데스카운트", value = "5개" , inline = True)
            embed.add_field(name = "물약 쿨타임", value = "없음", inline = True)
            embed.add_field(name = "페이즈 개수", value = "3개", inline = False)
            embed.add_field(name = "1페이즈 체력", value = "3,300,000,000 (33억)", inline = False)
            embed.add_field(name = "2페이즈 체력", value = "3,300,000,000 (33억)", inline = False)
            embed.add_field(name = "3페이즈 체력", value = "20,000,000,000 (200억)", inline = False)
            embed.add_field(name = "전체 체력", value = "26,600,000,000 (266억)", inline = False)
            embed.add_field(name = "방어율", value = "타격위치에 따라 달라짐", inline = True)
            embed.add_field(name = "파티격 요구스펙", value = "180레벨 이상", inline = False)
            embed.add_field(name = "솔격 요구스펙", value = "180레벨 이상", inline = False)
            embed.add_field(name = "결정석 가격", value = "[본섭] 135만 2000메소 \n[리부트] 405만 6000메소", inline = False)
            embed.add_field(name = "확정 드랍 보상", value = "없음 (십자코인 등 기초아이템은 존재)", inline = False)
            embed.add_field(name = "확률적 드랍 보상", value = "실버블라썸 링, 데아 시두스 이어링, 카오스 혼테일의 목걸이", inline = False)
            embed.add_field(name = "공략 영상 URL", value = "(추후 영상 첨부)", inline = False)
            embed.add_field(name = "패턴 정보", value = "https://namu.wiki/w/혼테일#s-5", inline = False)
            embed.set_thumbnail(url = "https://ww.namu.la/s/897a6c291fd033e8afc661c8b944c0e1cfab12c4be04add3676d17bc4d61379b199b4086a1596f48b245b252131e3a510105bc9b9387cfb7a7075c7963e0d08122a98578647e000040321a7ce5c32eedb8d05250194fd095ff5de96e1c697b3f")
            await message.channel.send(message.channel, embed=embed)
        # 반반
        elif InputData[1] == "반반" :
            await message.channel.send('노말 반반와 카오스 반반에 대한 정보를 출력합니다.')
            await message.channel.send('&보스정보 노말반반')
            await message.channel.send('&보스정보 카오스반반')
        elif InputData[1] == "노말반반" or InputData[1] == "노멀반반" :
            embed = discord.Embed(title = "보스몬스터 [노말 반반] 정보",description = "보스몬스터 [노말 반반]의 정보를 제공해드립니다.",color = 0x0000FF)
            embed.add_field(name = "입장 요구레벨", value = "Lv.125", inline = True)
            embed.add_field(name = "몬스터 레벨", value = "Lv.120", inline = True)
            embed.add_field(name = "제한시간", value = "8분 (변동가능)", inline = True)
            embed.add_field(name = "데스카운트", value = "5개" , inline = True)
            embed.add_field(name = "물약 쿨타임", value = "없음", inline = True)
            embed.add_field(name = "페이즈 개수", value = "3개 (구분되지 않음)", inline = False)
            embed.add_field(name = "전체 체력", value = "315,000,000 (3억 1500만)", inline = False)
            embed.add_field(name = "방어율", value = "50%", inline = True)
            embed.add_field(name = "파티격 요구스펙", value = "125레벨 이상", inline = False)
            embed.add_field(name = "솔격 요구스펙", value = "125레벨 이상", inline = False)
            embed.add_field(name = "결정석 가격", value = "[본섭] 96만 8000메소 \n[리부트] 290만 4000메소", inline = False)
            embed.add_field(name = "확정 드랍 보상", value = "이그드라실의 룬", inline = False)
            embed.add_field(name = "확률적 드랍 보상", value = "반반 투구, 반반과 함께(의자), 반반의 소울조각", inline = False)
            embed.add_field(name = "공략 영상 URL", value = "(추후 영상 첨부)", inline = False)
            embed.add_field(name = "패턴 정보", value = "https://namu.wiki/w/반반(메이플스토리)#s-4.3", inline = False)
            embed.set_thumbnail(url = "https://ww.namu.la/s/722e514c404916c5b7a0971d74247391f2ec8f1e27b01d202ab155c073c0dc3b4373f1261766fa28420fc28f5d7c9e9b5e4788ae5259615cdf402853c53bfc46805b4517f1fa1d85a1fd7630090003c62c9cac5aae3f59265bea5b881c938cb7")
            await message.channel.send(message.channel, embed=embed)
        elif InputData[1] == "카오스반반" or InputData[1] == "카반" :
            embed = discord.Embed(title = "보스몬스터 [카오스 반반] 정보",description = "보스몬스터 [카오스 반반]의 정보를 제공해드립니다.",color = 0x0000FF)
            embed.add_field(name = "입장 요구레벨", value = "Lv.180", inline = True)
            embed.add_field(name = "몬스터 레벨", value = "Lv.190", inline = True)
            embed.add_field(name = "제한시간", value = "10분 (변동가능)", inline = True)
            embed.add_field(name = "데스카운트", value = "5개" , inline = True)
            embed.add_field(name = "물약 쿨타임", value = "없음", inline = True)
            embed.add_field(name = "페이즈 개수", value = "4개 (구분되지 않음)", inline = False)
            embed.add_field(name = "전체 체력", value = "100,000,000,000 + 800,000,000 x n(내면세계 횟수) (1000억 + 8억 x n(내면세계 횟수))", inline = False)
            embed.add_field(name = "방어율", value = "100%", inline = True)
            embed.add_field(name = "파티격 요구스펙", value = "무릉 30층 이상", inline = False)
            embed.add_field(name = "솔격 요구스펙", value = "무릉 31층 이상", inline = False)
            embed.add_field(name = "결정석 가격", value = "[본섭] 1620만 메소 \n[리부트] 4860만 메소", inline = False)
            embed.add_field(name = "확정 드랍 보상", value = "카오스 이그드라실의 룬, 시간의 조각(150제 카룻상의와 교환가능)", inline = False)
            embed.add_field(name = "확률적 드랍 보상", value = "반반 투구, 카오스 반반 투구(럭키아이템), 반반과 함께(의자), 반반의 소울조각", inline = False)
            embed.add_field(name = "공략 영상 URL", value = "(추후 영상 첨부)", inline = False)
            embed.add_field(name="패턴 정보", value="https://namu.wiki/w/반반(메이플스토리)#s-4.3", inline=False)
            embed.set_thumbnail(url="https://ww.namu.la/s/722e514c404916c5b7a0971d74247391f2ec8f1e27b01d202ab155c073c0dc3b4373f1261766fa28420fc28f5d7c9e9b5e4788ae5259615cdf402853c53bfc46805b4517f1fa1d85a1fd7630090003c62c9cac5aae3f59265bea5b881c938cb7")
            await message.channel.send(message.channel, embed=embed)
        # 피에르
        elif InputData[1] == "피에르" :
            await message.channel.send('노말 피에르와 카오스 피에르에 대한 정보를 출력합니다.')
            await message.channel.send('&보스정보 노말피에르')
            await message.channel.send('&보스정보 카오스피에르')
        elif InputData[1] == "노말피에르" or InputData[1] == "노멀피에르" :
            embed = discord.Embed(title = "보스몬스터 [노말 피에르] 정보",description = "보스몬스터 [노말 피에르]의 정보를 제공해드립니다.",color = 0x0000FF)
            embed.add_field(name = "입장 요구레벨", value = "Lv.125", inline = True)
            embed.add_field(name = "몬스터 레벨", value = "Lv.120", inline = True)
            embed.add_field(name = "제한시간", value = "15분", inline = True)
            embed.add_field(name = "데스카운트", value = "5개" , inline = True)
            embed.add_field(name = "물약 쿨타임", value = "없음", inline = True)
            embed.add_field(name = "페이즈 개수", value = "2개 (구분되지 않음)", inline = False)
            embed.add_field(name = "전체 체력", value = "315,000,000 (3억 1500만)", inline = False)
            embed.add_field(name = "방어율", value = "50%", inline = True)
            embed.add_field(name = "파티격 요구스펙", value = "125레벨 이상", inline = False)
            embed.add_field(name = "솔격 요구스펙", value = "125레벨 이상", inline = False)
            embed.add_field(name = "결정석 가격", value = "[본섭] 96만 8000메소 \n[리부트] 290만 4000메소", inline = False)
            embed.add_field(name = "확정 드랍 보상", value = "이그드라실의 룬", inline = False)
            embed.add_field(name = "확률적 드랍 보상", value = "피에르 모자, 즐거운 피에르(의자), 피에르의 소울조각", inline = False)
            embed.add_field(name = "공략 영상 URL", value = "(추후 영상 첨부)", inline = False)
            embed.add_field(name = "패턴 정보", value = "https://namu.wiki/w/피에르(메이플스토리)#s-5.3", inline = False)
            embed.set_thumbnail(url = "https://w.namu.la/s/3e157db9dfe54ef1fc92c83914d99a4ac95d06369d9e713f93d9fec0e6382d7c4ce30225af402484fbe1e3cca5b57a4cd4df9370790f093ea973e695fc051e818cb2de873eff2ca329b469f177944ef119792cb05764259bf1d7e4083d258673")
            await message.channel.send(message.channel, embed=embed)
        elif InputData[1] == "카오스피에르" or InputData[1] == "카피" or InputData[1] == "카삐" :
            embed = discord.Embed(title = "보스몬스터 [카오스 피에르] 정보",description = "보스몬스터 [카오스 피에르]의 정보를 제공해드립니다.",color = 0x0000FF)
            embed.add_field(name = "입장 요구레벨", value = "Lv.180", inline = True)
            embed.add_field(name = "몬스터 레벨", value = "Lv.190", inline = True)
            embed.add_field(name = "제한시간", value = "20분", inline = True)
            embed.add_field(name = "데스카운트", value = "5개" , inline = True)
            embed.add_field(name = "물약 쿨타임", value = "없음", inline = True)
            embed.add_field(name = "페이즈 개수", value = "3개 (구분되지 않음)", inline = False)
            embed.add_field(name = "전체 체력", value = "80,000,000,000 + 24,000,000,000(분열시) + 8,000,000,000 x n(한쪽만 처치하고 부활한 횟수) (800억 + 240억 + 8억 x n)", inline = False)
            embed.add_field(name = "방어율", value = "80%", inline = True)
            embed.add_field(name = "파티격 요구스펙", value = "무릉 30층 이상", inline = False)
            embed.add_field(name = "솔격 요구스펙", value = "무릉 31~33층 이상 (극딜기, 바인드 유무에 따라 달라짐)", inline = False)
            embed.add_field(name = "결정석 가격", value = "[본섭] 1620만 메소 \n[리부트] 4860만 메소", inline = False)
            embed.add_field(name = "확정 드랍 보상", value = "카오스 이그드라실의 룬, 조롱의 조각(150제 카룻하의와 교환가능)", inline = False)
            embed.add_field(name = "확률적 드랍 보상", value = "피에르 모자, 카오스 피에르 모자(럭키아이템), 즐거운 피에르(의자), 피에르의 소울조각", inline = False)
            embed.add_field(name = "공략 영상 URL", value = "(추후 영상 첨부)", inline = False)
            embed.add_field(name="패턴 정보", value="https://namu.wiki/w/피에르(메이플스토리)#s-5.3", inline=False)
            embed.set_thumbnail(url="https://w.namu.la/s/3e157db9dfe54ef1fc92c83914d99a4ac95d06369d9e713f93d9fec0e6382d7c4ce30225af402484fbe1e3cca5b57a4cd4df9370790f093ea973e695fc051e818cb2de873eff2ca329b469f177944ef119792cb05764259bf1d7e4083d258673")
            await message.channel.send(message.channel, embed=embed)
        # 블러디퀸
        elif InputData[1] == "블러디퀸" :
            await message.channel.send('노말 블러디퀸와 카오스 블러디퀸에 대한 정보를 출력합니다.')
            await message.channel.send('&보스정보 노말블러디퀸')
            await message.channel.send('&보스정보 카오스블러디퀸')
        elif InputData[1] == "노말블러디퀸" or InputData[1] == "노멀블러디퀸" :
            embed = discord.Embed(title = "보스몬스터 [노말 블러디 퀸] 정보",description = "보스몬스터 [노말 블러디 퀸]의 정보를 제공해드립니다.",color = 0x0000FF)
            embed.add_field(name = "입장 요구레벨", value = "Lv.125", inline = True)
            embed.add_field(name = "몬스터 레벨", value = "Lv.120", inline = True)
            embed.add_field(name = "제한시간", value = "15분", inline = True)
            embed.add_field(name = "데스카운트", value = "5개" , inline = True)
            embed.add_field(name = "물약 쿨타임", value = "없음", inline = True)
            embed.add_field(name = "페이즈 개수", value = "4개 (구분되지 않음, 반복가능)", inline = False)
            embed.add_field(name = "전체 체력", value = "315,000,000 (3억 1500만)", inline = False)
            embed.add_field(name = "방어율", value = "50%", inline = True)
            embed.add_field(name = "파티격 요구스펙", value = "125레벨 이상", inline = False)
            embed.add_field(name = "솔격 요구스펙", value = "125레벨 이상", inline = False)
            embed.add_field(name = "결정석 가격", value = "[본섭] 96만 8000메소 \n[리부트] 290만 4000메소", inline = False)
            embed.add_field(name = "확정 드랍 보상", value = "이그드라실의 룬", inline = False)
            embed.add_field(name = "확률적 드랍 보상", value = "퀸의 티아라, 무서워요 퀸(의자), 블러디 퀸의 소울조각", inline = False)
            embed.add_field(name = "공략 영상 URL", value = "(추후 영상 첨부)", inline = False)
            embed.add_field(name = "패턴 정보", value = "https://namu.wiki/w/블러디%20퀸#s-5.3", inline = False)
            embed.set_thumbnail(url = "https://w.namu.la/s/c5b7e7e2d11451550bc13b70e11b1c3dd5ad9a85837c2d38bd9670176a7d5c423943bca807b841839c10f6a7310bfcf20b358d084175529eee7521e0408aee169c6369064de2f14f0eb4212fe69ba0a370f39d4cca8c92bf02e3a380cf539139")
            await message.channel.send(message.channel, embed=embed)
        elif InputData[1] == "카오스블러디퀸" or InputData[1] == "카퀸" or InputData[1] == "카블퀸" :
            embed = discord.Embed(title = "보스몬스터 [카오스 블러디 퀸] 정보",description = "보스몬스터 [카오스 블러디 퀸]의 정보를 제공해드립니다.",color = 0x0000FF)
            embed.add_field(name = "입장 요구레벨", value = "Lv.180", inline = True)
            embed.add_field(name = "몬스터 레벨", value = "Lv.190", inline = True)
            embed.add_field(name = "제한시간", value = "20분", inline = True)
            embed.add_field(name = "데스카운트", value = "5개" , inline = True)
            embed.add_field(name = "물약 쿨타임", value = "없음", inline = True)
            embed.add_field(name = "페이즈 개수", value = "4개 (구분되지 않음, 반복가능)", inline = False)
            embed.add_field(name = "전체 체력", value = "140,000,000,000 (1400억)", inline = False)
            embed.add_field(name = "방어율", value = "120%", inline = True)
            embed.add_field(name = "파티격 요구스펙", value = "무릉 30층 이상", inline = False)
            embed.add_field(name = "솔격 요구스펙", value = "[비숍 등 디스펠 혹은 상태이상 방어/무적기가 있을 경우] 무릉 30층 이상 \n[그 외] 무릉 31~33층 이상", inline = False)
            embed.add_field(name = "결정석 가격", value = "[본섭] 1620만 메소 \n[리부트] 4860만 메소", inline = False)
            embed.add_field(name = "확정 드랍 보상", value = "카오스 이그드라실의 룬, 절규의 조각(150제 카룻모자와 교환가능)", inline = False)
            embed.add_field(name = "확률적 드랍 보상", value = "퀸의 티아라, 카오스 퀸의 티아라(럭키아이템), 무서워요 퀸(의자), 블러디 퀸의 소울조각", inline = False)
            embed.add_field(name = "공략 영상 URL", value = "(추후 영상 첨부)", inline = False)
            embed.add_field(name="패턴 정보", value="https://namu.wiki/w/블러디%20퀸#s-5.3", inline=False)
            embed.set_thumbnail(url="https://w.namu.la/s/c5b7e7e2d11451550bc13b70e11b1c3dd5ad9a85837c2d38bd9670176a7d5c423943bca807b841839c10f6a7310bfcf20b358d084175529eee7521e0408aee169c6369064de2f14f0eb4212fe69ba0a370f39d4cca8c92bf02e3a380cf539139")
            await message.channel.send(message.channel, embed=embed)
        # 벨룸
        elif InputData[1] == "벨룸":
            await message.channel.send('노말 벨룸과 카오스 벨룸에 대한 정보를 출력합니다.')
            await message.channel.send('&보스정보 노말벨룸')
            await message.channel.send('&보스정보 카오스벨룸')
        elif InputData[1] == "노말벨룸" or InputData[1] == "노멀벨룸":
            embed = discord.Embed(title="보스몬스터 [노말 벨룸] 정보", description="보스몬스터 [노말 벨룸]의 정보를 제공해드립니다.",color=0x0000FF)
            embed.add_field(name="입장 요구레벨", value="Lv.125", inline=True)
            embed.add_field(name="몬스터 레벨", value="Lv.130", inline=True)
            embed.add_field(name="제한시간", value="15분", inline=True)
            embed.add_field(name="데스카운트", value="5개", inline=True)
            embed.add_field(name="물약 쿨타임", value="없음", inline=True)
            embed.add_field(name="페이즈 개수", value="3개 (구분되지 않음)", inline=False)
            embed.add_field(name="전체 체력", value="550,000,000 (5억 5000만)", inline=False)
            embed.add_field(name="방어율", value="55%", inline=True)
            embed.add_field(name="파티격 요구스펙", value="125레벨 이상", inline=False)
            embed.add_field(name="솔격 요구스펙", value="125레벨 이상", inline=False)
            embed.add_field(name="결정석 가격", value="[본섭] 96만 8000메소 \n[리부트] 290만 4000메소", inline=False)
            embed.add_field(name="확정 드랍 보상", value="이그드라실의 룬", inline=False)
            embed.add_field(name="확률적 드랍 보상", value="벨룸의 헬름, 기암괴석 의자(의자), 벨룸의 소울조각", inline=False)
            embed.add_field(name="공략 영상 URL", value="(추후 영상 첨부)", inline=False)
            embed.add_field(name="패턴 정보", value="https://namu.wiki/w/벨룸#s-4.3", inline=False)
            embed.set_thumbnail(url="https://ww.namu.la/s/ca7c1e12362057357414a9f64a7965a411a9cbf96ac8e637cb0830954017269c381a873bd02ef41b2e3154a389d961370cbfaa04302cdbd364c9aa29413f919e38e84901f53bb21c47221cacc7e846974e9aa270d6b4acf7757cf97e4bf4df75")
            await message.channel.send(message.channel, embed=embed)
        elif InputData[1] == "카오스벨룸" or InputData[1] == "카벨" or InputData[1] == "카벨룸":
            embed = discord.Embed(title="보스몬스터 [카오스 벨룸] 정보", description="보스몬스터 [카오스 벨룸]의 정보를 제공해드립니다.",color=0x0000FF)
            embed.add_field(name="입장 요구레벨", value="Lv.180", inline=True)
            embed.add_field(name="몬스터 레벨", value="Lv.190", inline=True)
            embed.add_field(name="제한시간", value="20분", inline=True)
            embed.add_field(name="데스카운트", value="5개", inline=True)
            embed.add_field(name="물약 쿨타임", value="없음", inline=True)
            embed.add_field(name="페이즈 개수", value="4개 (구분되지 않음)", inline=False)
            embed.add_field(name="전체 체력", value="200,000,000,000 (2000억)", inline=False)
            embed.add_field(name="방어율", value="200%", inline=True)
            embed.add_field(name="파티격 요구스펙", value="무릉 30층 이상", inline=False)
            embed.add_field(name="솔격 요구스펙", value="무릉 34~6층 이상",inline=False)
            embed.add_field(name="결정석 가격", value="[본섭] 2101만 2500메소 \n[리부트] 6303만 7500메소", inline=False)
            embed.add_field(name="확정 드랍 보상", value="카오스 이그드라실의 룬, 파멸의 조각(150제 카룻무기와 교환가능)", inline=False)
            embed.add_field(name="확률적 드랍 보상", value="벨룸의 헬름, 카오스 벨룸의 헬름(럭키아이템), 기암괴석 의자(의자), 벨룸의 소울조각", inline=False)
            embed.add_field(name="공략 영상 URL", value="(추후 영상 첨부)", inline=False)
            embed.add_field(name="패턴 정보", value="https://namu.wiki/w/벨룸#s-4.3", inline=False)
            embed.set_thumbnail(url="https://ww.namu.la/s/ca7c1e12362057357414a9f64a7965a411a9cbf96ac8e637cb0830954017269c381a873bd02ef41b2e3154a389d961370cbfaa04302cdbd364c9aa29413f919e38e84901f53bb21c47221cacc7e846974e9aa270d6b4acf7757cf97e4bf4df75")
            await message.channel.send(message.channel, embed=embed)
        # 아카이럼
        elif InputData[1] == "아카이럼":
            await message.channel.send('이지 아카이럼과 노말 아카이럼에 대한 정보를 출력합니다.')
            await message.channel.send('&보스정보 이지아카이럼')
            await message.channel.send('&보스정보 노말아카이럼')
        elif InputData[1] == "이지아카이럼" or InputData[1] == "이지아카":
            embed = discord.Embed(title="보스몬스터 [이지 아카이럼] 정보", description="보스몬스터 [이지 아카이럼]의 정보를 제공해드립니다.",color=0x0000FF)
            embed.add_field(name="입장 요구레벨", value="Lv.130", inline=True)
            embed.add_field(name="몬스터 레벨", value="Lv.130", inline=True)
            embed.add_field(name="제한시간", value="30분", inline=True)
            embed.add_field(name="데스카운트", value="5개", inline=True)
            embed.add_field(name="물약 쿨타임", value="없음", inline=True)
            embed.add_field(name="페이즈 개수", value="페이즈로 구분되지 않음", inline=False)
            embed.add_field(name="전체 체력", value="2,100,000,000 (21억)", inline=False)
            embed.add_field(name="방어율", value="60%", inline=True)
            embed.add_field(name="파티격 요구스펙", value="150레벨 이상", inline=False)
            embed.add_field(name="솔격 요구스펙", value="170레벨 이상", inline=False)
            embed.add_field(name="결정석 가격", value="[본섭] 115만 2000메소 \n[리부트] 345만 6000메소", inline=False)
            embed.add_field(name="확정 드랍 보상", value="아카이럼의 반지 제작 레시피", inline=False)
            embed.add_field(name="확률적 드랍 보상", value="아카이럼의 소울조각, 매커네이터 펜던트 \n[본섭] 비틀린 시간의 파편", inline=False)
            embed.add_field(name="공략 영상 URL", value="(추후 영상 첨부)", inline=False)
            embed.add_field(name="패턴 정보", value="https://namu.wiki/w/아카이럼/보스%20몬스터#s-4", inline=False)
            embed.set_thumbnail(url="https://ww.namu.la/s/d906a3913407734957a24ceee54fc972eeacaeae23c1dc0bffd9149dd73154ec92ec6e94e6df1dc3743c417625a43bb4cbc402956dc0976fe99c06034ab3531a730c97d1ab13a6f57016bef699299baed02f7cd1ba3de5bf663ad3503b223b04")
            await message.channel.send(message.channel, embed=embed)
        elif InputData[1] == "노말아카이럼" or InputData[1] == "노아" or InputData[1] == "아카":
            embed = discord.Embed(title="보스몬스터 [노말 아카이럼] 정보", description="보스몬스터 [노말 아카이럼]의 정보를 제공해드립니다.",color=0x0000FF)
            embed.add_field(name="입장 요구레벨", value="Lv.140", inline=True)
            embed.add_field(name="몬스터 레벨", value="Lv.170", inline=True)
            embed.add_field(name="제한시간", value="30분", inline=True)
            embed.add_field(name="데스카운트", value="5개", inline=True)
            embed.add_field(name="물약 쿨타임", value="없음", inline=True)
            embed.add_field(name="페이즈 개수", value="페이즈로 구분되지 않음", inline=False)
            embed.add_field(name="전체 체력", value="12,600,000,000 (126억)", inline=False)
            embed.add_field(name="방어율", value="90%", inline=True)
            embed.add_field(name="파티격 요구스펙", value="무릉 20층 이상", inline=False)
            embed.add_field(name="솔격 요구스펙", value="무릉 20층 이상",inline=False)
            embed.add_field(name="결정석 가격", value="[본섭] 252만 500메소 \n[리부트] 756만 1500메소", inline=False)
            embed.add_field(name="확정 드랍 보상", value="아카이럼의 반지 제작 레시피", inline=False)
            embed.add_field(name="확률적 드랍 보상", value="도미네이터 펜던트, 매커네이터 펜던트, 아카이럼의 소울조각 \n[본섭] 비틀린 시간의 파편", inline=False)
            embed.add_field(name="공략 영상 URL", value="(추후 영상 첨부)", inline=False)
            embed.add_field(name="패턴 정보", value="https://namu.wiki/w/아카이럼/보스%20몬스터#s-4", inline=False)
            embed.set_thumbnail(url="https://ww.namu.la/s/d906a3913407734957a24ceee54fc972eeacaeae23c1dc0bffd9149dd73154ec92ec6e94e6df1dc3743c417625a43bb4cbc402956dc0976fe99c06034ab3531a730c97d1ab13a6f57016bef699299baed02f7cd1ba3de5bf663ad3503b223b04")
            await message.channel.send(message.channel, embed=embed)
        # 반 레온
        elif InputData[1] == "반레온" :
            await message.channel.send('이지/노말/하드 반 레온에 대한 정보를 출력합니다.')
            await message.channel.send('&보스정보 이지반레온')
            await message.channel.send('&보스정보 노말반레온')
            await message.channel.send('&보스정보 하드반레온')
            return
        elif InputData[1] == "이지반레온":
            embed = discord.Embed(title="보스몬스터 [이지 반 레온] 정보", description="보스몬스터 [이지 반 레온]의 정보를 제공해드립니다.",color=0x0000FF)
            embed.add_field(name="입장 요구레벨", value="Lv.125", inline=True)
            embed.add_field(name="몬스터 레벨", value="Lv.120", inline=True)
            embed.add_field(name="제한시간", value="30분", inline=True)
            embed.add_field(name="데스카운트", value="5개", inline=True)
            embed.add_field(name="물약 쿨타임", value="30초", inline=True)
            embed.add_field(name="페이즈 개수", value="페이즈로 구분되지 않음", inline=False)
            embed.add_field(name="전체 체력", value="700,000,000 (7억)", inline=False)
            embed.add_field(name="방어율", value="50%", inline=True)
            embed.add_field(name="파티격 요구스펙", value="125레벨 이상", inline=False)
            embed.add_field(name="솔격 요구스펙", value="125레벨 이상", inline=False)
            embed.add_field(name="결정석 가격", value="[본섭] 105만 8000메소 \n[리부트] 317만 4000메소", inline=False)
            embed.add_field(name="확정 드랍 보상", value="로얄 반 레온 메달", inline=False)
            embed.add_field(name="확률적 드랍 보상", value="반 레온의 소울조각", inline=False)
            embed.add_field(name="공략 영상 URL", value="(추후 영상 첨부)", inline=False)
            embed.add_field(name="패턴 정보", value="https://namu.wiki/w/반%20레온/보스%20몬스터#s-3", inline=False)
            embed.set_thumbnail(url="https://w.namu.la/s/6323fd3b8ef2d475289fb19ecda35e291ed43f399f59fc5610a5c60c944c1e8844aea0c3b929df8a4cecab4b65565eba015a72ad7c7471ae7ee75a9301090573070a8ca899d90b1975d826677083e139522f96f56fb48b2373704904664f4411")
            await message.channel.send(message.channel, embed=embed)
        elif InputData[1] == "노말반레온" or InputData[1] == "노반":
            embed = discord.Embed(title="보스몬스터 [노말 반 레온] 정보", description="보스몬스터 [노말 반 레온]의 정보를 제공해드립니다.",color=0x0000FF)
            embed.add_field(name="입장 요구레벨", value="Lv.125", inline=True)
            embed.add_field(name="몬스터 레벨", value="Lv.130", inline=True)
            embed.add_field(name="제한시간", value="30분", inline=True)
            embed.add_field(name="데스카운트", value="5개", inline=True)
            embed.add_field(name="물약 쿨타임", value="30초", inline=True)
            embed.add_field(name="페이즈 개수", value="페이즈로 구분되지 않음", inline=False)
            embed.add_field(name="전체 체력", value="6,300,000,000 (63억)", inline=False)
            embed.add_field(name="방어율", value="80%", inline=True)
            embed.add_field(name="파티격 요구스펙", value="무릉 10층 이상", inline=False)
            embed.add_field(name="솔격 요구스펙", value="무릉 10층 이상",inline=False)
            embed.add_field(name="결정석 가격", value="[본섭] 145만 8000메소 \n[리부트] 437만 4000메소", inline=False)
            embed.add_field(name="확정 드랍 보상", value="로얄 반 레온 메달", inline=False)
            embed.add_field(name="확률적 드랍 보상", value="반 레온의 소울조각", inline=False)
            embed.add_field(name="공략 영상 URL", value="(추후 영상 첨부)", inline=False)
            embed.add_field(name="패턴 정보", value="https://namu.wiki/w/반%20레온/보스%20몬스터#s-3", inline=False)
            embed.set_thumbnail(url="https://w.namu.la/s/6323fd3b8ef2d475289fb19ecda35e291ed43f399f59fc5610a5c60c944c1e8844aea0c3b929df8a4cecab4b65565eba015a72ad7c7471ae7ee75a9301090573070a8ca899d90b1975d826677083e139522f96f56fb48b2373704904664f4411")
            await message.channel.send(message.channel, embed=embed)
        elif InputData[1] == "하드반레온" or InputData[1] == "하반":
            embed = discord.Embed(title="보스몬스터 [하드 반 레온] 정보", description="보스몬스터 [하드 반 레온]의 정보를 제공해드립니다.",color=0x0000FF)
            embed.add_field(name="입장 요구레벨", value="Lv.125", inline=True)
            embed.add_field(name="몬스터 레벨", value="Lv.140", inline=True)
            embed.add_field(name="제한시간", value="30분", inline=True)
            embed.add_field(name="데스카운트", value="5개", inline=True)
            embed.add_field(name="물약 쿨타임", value="30초", inline=True)
            embed.add_field(name="페이즈 개수", value="페이즈로 구분되지 않음", inline=False)
            embed.add_field(name="전체 체력", value="10,500,000,000 (105억)", inline=False)
            embed.add_field(name="방어율", value="100%", inline=True)
            embed.add_field(name="파티격 요구스펙", value="무릉 20층 이상", inline=False)
            embed.add_field(name="솔격 요구스펙", value="무릉 20층 이상",inline=False)
            embed.add_field(name="결정석 가격", value="[본섭] 245만 메소 \n[리부트] 735만 메소", inline=False)
            embed.add_field(name="확정 드랍 보상", value="이피아의 장신구 (1~3개)", inline=False)
            embed.add_field(name="확률적 드랍 보상", value="반 레온의 소울조각, 로얄 반 레온 장비아이템", inline=False)
            embed.add_field(name="공략 영상 URL", value="(추후 영상 첨부)", inline=False)
            embed.add_field(name="패턴 정보", value="https://namu.wiki/w/반%20레온/보스%20몬스터#s-3", inline=False)
            embed.set_thumbnail(url="https://w.namu.la/s/6323fd3b8ef2d475289fb19ecda35e291ed43f399f59fc5610a5c60c944c1e8844aea0c3b929df8a4cecab4b65565eba015a72ad7c7471ae7ee75a9301090573070a8ca899d90b1975d826677083e139522f96f56fb48b2373704904664f4411")
            await message.channel.send(message.channel, embed=embed)
        # 카웅
        elif InputData[1] == "카웅" or InputData[1] == "노말카웅" or InputData[1] == "노멀카웅" :
            embed = discord.Embed(title = "보스몬스터 [카웅] 정보",description = "보스몬스터 [카웅]의 정보를 제공해드립니다.",color = 0x0000FF)
            embed.add_field(name = "입장 요구레벨", value = "Lv.180", inline = True)
            embed.add_field(name = "몬스터 레벨", value = "Lv.180", inline = True)
            embed.add_field(name = "제한시간", value = "30분", inline = True)
            embed.add_field(name = "데스카운트", value = "5개" , inline = True)
            embed.add_field(name = "물약 쿨타임", value = "없음", inline = True)
            embed.add_field(name = "페이즈 개수", value = "페이즈로 구분되지 않음", inline = False)
            embed.add_field(name = "전체 체력", value = "1,680,000,000 (16억 8000만)", inline = False)
            embed.add_field(name = "방어율", value = "60%", inline = True)
            embed.add_field(name = "파티격 요구스펙", value = "200레벨 이상", inline = False)
            embed.add_field(name = "솔격 요구스펙", value = "200레벨 이상", inline = False)
            embed.add_field(name = "결정석 가격", value = "[본섭] 125만 메소 \n[리부트] 375만 메소", inline = False)
            embed.add_field(name = "확정 드랍 보상", value = "카웅 부품", inline = False)
            embed.add_field(name = "확률적 드랍 보상", value = "없음", inline = False)
            embed.add_field(name = "공략 영상 URL", value = "(추후 영상 첨부)", inline = False)
            embed.add_field(name = "패턴 정보", value = "https://namu.wiki/w/카웅#s-3", inline = False)
            embed.set_thumbnail(url = "https://ww.namu.la/s/8dbd2652864b3059634eca2c765b410f6688c62e984b24840e46a0b2c1274af28e8d9cf77fed4124d7834655a87699e03ee35a13b70a841c57ca1bb7a9549c35489c076adeb9658ec057aaeb812f1778714d8782c3f87fa9f4ec7d376d7d9122")
            await message.channel.send(message.channel, embed=embed)
        # 핑크빈
        elif InputData[1] == "핑크빈" :
            await message.channel.send('노말 핑크빈와 카오스 핑크빈에 대한 정보를 출력합니다.')
            await message.channel.send('&보스정보 노말핑크빈')
            await message.channel.send('&보스정보 카오스핑크빈')
        elif InputData[1] == "노말핑크빈" or InputData[1] == "노멀핑크빈" :
            embed = discord.Embed(title = "보스몬스터 [노말 핑크빈] 정보",description = "보스몬스터 [노말 핑크빈]의 정보를 제공해드립니다.",color = 0x0000FF)
            embed.add_field(name = "입장 요구레벨", value = "Lv.160", inline = True)
            embed.add_field(name = "몬스터 레벨", value = "Lv.180", inline = True)
            embed.add_field(name = "제한시간", value = "30분", inline = True)
            embed.add_field(name = "데스카운트", value = "5개" , inline = True)
            embed.add_field(name = "물약 쿨타임", value = "없음", inline = True)
            embed.add_field(name = "페이즈 개수", value = "2개 (구분되지 않음)", inline = False)
            embed.add_field(name = "석상 체력", value = "5,550,000,000 (55억 5천만)", inline = False)
            embed.add_field(name = "본체 체력", value = "2,100,000,000 (21억)", inline = False)
            embed.add_field(name = "전체 체력", value = "7,650,000,000 (76억 5천만)", inline = False)
            embed.add_field(name = "방어율", value = "70%", inline = True)
            embed.add_field(name = "파티격 요구스펙", value = "180레벨 이상", inline = False)
            embed.add_field(name = "솔격 요구스펙", value = "180레벨 이상", inline = False)
            embed.add_field(name = "결정석 가격", value = "[본섭] 140만 4500메소 \n[리부트] 421만 3500메소", inline = False)
            embed.add_field(name = "확정 드랍 보상", value = "없음 (십자코인 등 기초아이템은 존재)", inline = False)
            embed.add_field(name = "확률적 드랍 보상", value = "핑크빈의 소울조각, 핑크빛 성배, 골든 클로버 벨트, 블랙빈 마크", inline = False)
            embed.add_field(name = "공략 영상 URL", value = "(추후 영상 첨부)", inline = False)
            embed.add_field(name = "패턴 정보", value = "https://namu.wiki/w/핑크빈#s-5", inline = False)
            embed.set_thumbnail(url = "https://ww.namu.la/s/308fb8682aa92c0683f81959ec244d0cd1a4573b86b573f59efa4eb8b83a5bf9b9b128fc3ff71301acf6cbf1bfa7c5fed5a5d46359271297fad568d1fbabb1091cc1470149a04c80e4b7a5e590450cab95522082714cddc4f3441046e37fdb2e")
            await message.channel.send(message.channel, embed=embed)
        elif InputData[1] == "카오스핑크빈" or InputData[1] == "카핑" :
            embed = discord.Embed(title = "보스몬스터 [카오스 핑크빈] 정보",description = "보스몬스터 [카오스 핑크빈]의 정보를 제공해드립니다.",color = 0x0000FF)
            embed.add_field(name = "입장 요구레벨", value = "Lv.170", inline = True)
            embed.add_field(name = "몬스터 레벨", value = "Lv.190", inline = True)
            embed.add_field(name = "제한시간", value = "30분", inline = True)
            embed.add_field(name = "데스카운트", value = "5개" , inline = True)
            embed.add_field(name = "물약 쿨타임", value = "없음", inline = True)
            embed.add_field(name = "페이즈 개수", value = "4개 (구분되지 않음)", inline = False)
            embed.add_field(name = "석상 체력", value = "134,400,000,000 (1344억)", inline = False)
            embed.add_field(name = "본체1 체력", value = "12,600,000,000 (126억)", inline = False)
            embed.add_field(name = "본체2 체력", value = "23,100,000,000 (231억)", inline = False)
            embed.add_field(name = "본체3 체력", value = "33,600,000,000 (336억)", inline = False)
            embed.add_field(name = "전체 체력", value = "203,700,000,000 (2037억)", inline = False)
            embed.add_field(name = "방어율", value = "100%", inline = True)
            embed.add_field(name = "파티격 요구스펙", value = "무릉 30층 이상", inline = False)
            embed.add_field(name = "솔격 요구스펙", value = "무릉 33층 이상", inline = False)
            embed.add_field(name = "결정석 가격", value = "[본섭] 1280만 메소 \n[리부트] 3840만 메소", inline = False)
            embed.add_field(name = "확정 드랍 보상", value = "카오스 핑크빈 방어구", inline = False)
            embed.add_field(name = "확률적 드랍 보상", value = "핑크빈의 소울조각, 핑크빛 성배, 골든 클로버 벨트, 블랙빈 마크", inline = False)
            embed.add_field(name = "공략 영상 URL", value = "(추후 영상 첨부)", inline = False)
            embed.add_field(name = "패턴 정보", value = "https://namu.wiki/w/핑크빈#s-5", inline = False)
            embed.set_thumbnail(url = "https://ww.namu.la/s/308fb8682aa92c0683f81959ec244d0cd1a4573b86b573f59efa4eb8b83a5bf9b9b128fc3ff71301acf6cbf1bfa7c5fed5a5d46359271297fad568d1fbabb1091cc1470149a04c80e4b7a5e590450cab95522082714cddc4f3441046e37fdb2e")
            await message.channel.send(message.channel, embed=embed)
        # 시그너스
        elif InputData[1] == "시그너스" :
            await message.channel.send('이지시그너스와 노말 시그너스에 대한 정보를 출력합니다.')
            await message.channel.send('&보스정보 이지시그너스')
            await message.channel.send('&보스정보 노말시그너스')
            return
        elif InputData[1] == "이지시그너스" or InputData[1] == "이시" or InputData[1] == "이지시그" or InputData[1] == "이지여제" :
            embed = discord.Embed(title = "보스몬스터 [이지 시그너스] 정보",description = "보스몬스터 [이지 시그너스]의 정보를 제공해드립니다.",color = 0x0000FF)
            embed.add_field(name = "입장 요구레벨", value = "Lv.140", inline = True)
            embed.add_field(name = "몬스터 레벨", value = "Lv.140", inline = True)
            embed.add_field(name = "제한시간", value = "30분", inline = True)
            embed.add_field(name = "데스카운트", value = "5개" , inline = True)
            embed.add_field(name = "물약 쿨타임", value = "15초", inline = True)
            embed.add_field(name = "페이즈 개수", value = "페이즈로 구분되지 않음", inline = False)
            embed.add_field(name = "전체 체력", value = "10,500,000,000 (105억)", inline = False)
            embed.add_field(name = "방어율", value = "100%", inline = True)
            embed.add_field(name = "파티격 요구스펙", value = "180레벨 이상", inline = False)
            embed.add_field(name = "솔격 요구스펙", value = "180레벨 이상", inline = False)
            embed.add_field(name = "결정석 가격", value = "[본섭] 911만 2500메소 \n[리부트] 2733만 7500메소", inline = False)
            embed.add_field(name = "확정 드랍 보상", value = "검은 파괴의 조각(140제 여제 방어구와 교환), 검은 수호의 조각(140제 여제 무기와 교환), 꿈의 돌", inline = False)
            embed.add_field(name = "확률적 드랍 보상", value = "시그너스의 소울조각, 140제 여제 방어구/무기 레시피", inline = False)
            embed.add_field(name = "공략 영상 URL", value = "(추후 영상 첨부)", inline = False)
            embed.add_field(name = "패턴 정보", value = "https://namu.wiki/w/시그너스(메이플스토리)/보스%20몬스터/#s-5", inline = False)
            embed.set_thumbnail(url = "https://w.namu.la/s/88dc6f4e3f9689457f4ffb4ab0e6985dd319431b1a7ba8309da60316abf24587ebc9c84ba08b5a0cb0b9a94d77725a4f82f2f83f4039e7bf2ef28b3058b13d61e3b3a9862950281d688a0f7dc85fa37a5c3b092d8ea930bfd6efb56dea0bb345")
            await message.channel.send(message.channel, embed=embed)
        elif InputData[1] == "노말시그너스" or InputData[1] == "여제" or InputData[1] == "노말여제":
            embed = discord.Embed(title="보스몬스터 [노말 시그너스] 정보", description="보스몬스터 [노말 시그너스]의 정보를 제공해드립니다.",color=0x0000FF)
            embed.add_field(name="입장 요구레벨", value="Lv.165", inline=True)
            embed.add_field(name="몬스터 레벨", value="Lv.190", inline=True)
            embed.add_field(name="제한시간", value="30분", inline=True)
            embed.add_field(name="데스카운트", value="5개", inline=True)
            embed.add_field(name="물약 쿨타임", value="30초", inline=True)
            embed.add_field(name="페이즈 개수", value="페이즈로 구분되지 않음", inline=False)
            embed.add_field(name="전체 체력", value="63,000,000,000 (630억)", inline=False)
            embed.add_field(name="방어율", value="100%", inline=True)
            embed.add_field(name="파티격 요구스펙", value="무릉 30층 이상", inline=False)
            embed.add_field(name="솔격 요구스펙", value="무릉 33층 이상", inline=False)
            embed.add_field(name="결정석 가격", value="[본섭] 1445만 메소 \n[리부트] 4335만 메소", inline=False)
            embed.add_field(name="확정 드랍 보상", value="검은 파괴의 조각(140제 여제 방어구와 교환), 검은 수호의 조각(140제 여제 무기와 교환), 꿈의 돌",inline=False)
            embed.add_field(name="확률적 드랍 보상", value="시그너스의 소울조각, 140제 여제 방어구/무기 레시피, 140제 여제 견장", inline=False)
            embed.add_field(name="공략 영상 URL", value="(추후 영상 첨부)", inline=False)
            embed.add_field(name="패턴 정보", value="https://namu.wiki/w/시그너스(메이플스토리)/보스%20몬스터/#s-5", inline=False)
            embed.set_thumbnail(url="https://w.namu.la/s/88dc6f4e3f9689457f4ffb4ab0e6985dd319431b1a7ba8309da60316abf24587ebc9c84ba08b5a0cb0b9a94d77725a4f82f2f83f4039e7bf2ef28b3058b13d61e3b3a9862950281d688a0f7dc85fa37a5c3b092d8ea930bfd6efb56dea0bb345")
            await message.channel.send(message.channel, embed=embed)
        # 루시드
        elif InputData[1] == "루시드" :
            await message.channel.send('이지/노말/하드 루시드에 대한 정보를 출력합니다.')
            await message.channel.send('&보스정보 이지루시드')
            await message.channel.send('&보스정보 노말루시드')
            await message.channel.send('&보스정보 하드루시드')
            return
        elif InputData[1] == "이지루시드" or InputData[1] == "이룻" or InputData[1] == "이루시" or InputData[1] == "이루시드":
            embed = discord.Embed(title = "보스몬스터 [이지 루시드] 정보",description = "보스몬스터 [이지 루시드]의 정보를 제공해드립니다.",color = 0x0000FF)
            embed.add_field(name = "입장 요구레벨", value = "Lv.220", inline = True)
            embed.add_field(name = "몬스터 레벨", value = "Lv.230", inline = True)
            embed.add_field(name = "제한시간", value = "30분", inline = True)
            embed.add_field(name = "데스카운트", value = "10개", inline = True)
            embed.add_field(name = "물약 쿨타임", value = "5초", inline = True)
            embed.add_field(name = "요구 아케인포스", value = "360", inline = True)
            embed.add_field(name = "페이즈 개수", value = "2개", inline = False)
            embed.add_field(name = "1페이즈 체력", value = "6,000,000,000,000 (6조)", inline = False)
            embed.add_field(name = "2페이즈 체력", value = "6,000,000,000,000 (6조)", inline = False)
            embed.add_field(name = "전체 체력", value = "12,000,000,000,000 (12조)", inline = False)
            embed.add_field(name = "방어율", value = "300%", inline = True)
            embed.add_field(name = "파티격 요구스펙", value = "[비숍] 220레벨 이상 \n[타 직업] 230레벨 이상 및 무릉 44~45층 이상, 아케인포스 360 이상", inline = False)
            embed.add_field(name = "솔격 요구스펙", value = "[최소컷] 47층 이상", inline = False)
            embed.add_field(name = "결정석 가격", value = "[본섭] 3511만 2500메소 \n[리부트] 1억 533만 7500메소", inline = False)
            embed.add_field(name = "확정 드랍 보상", value = "[본섭] 수상한 에디셔널 큐브 \n[리부트] 장인의 큐브", inline = False)
            embed.add_field(name = "확률적 드랍 보상", value = "루시드의 소울조각", inline = False)
            embed.add_field(name = "공략 영상 URL", value = "(추후 추가예정)", inline = False)
            embed.add_field(name = "패턴 정보", value = "https://namu.wiki/w/루시드(메이플스토리)/보스%20몬스터#s-3", inline = False)
            embed.set_thumbnail(url = "https://w.namu.la/s/9af69355d0af6bc2e1fd4284e433090317c1aeb21c43d87658bd071ac759a09971ee9957326e0978d2eef0bbd2ad969566df0f5251327999bd873327562e86eb3b779b34f04fefe2c7c577ba37e6476263fa46b1f5873d400e76438d964d288a")
            await message.channel.send(message.channel, embed=embed)
        elif InputData[1] == "노말루시드" or InputData[1] == "노룻" or InputData[1] == "노루시" or InputData[1] == "노루시드" or InputData[1] == "노멀루시드":
            embed = discord.Embed(title="보스몬스터 [노말 루시드] 정보", description="보스몬스터 [노말 루시드]의 정보를 제공해드립니다.", color=0x0000FF)
            embed.add_field(name="입장 요구레벨", value="Lv.220", inline=True)
            embed.add_field(name="몬스터 레벨", value="Lv.230", inline=True)
            embed.add_field(name="제한시간", value="30분", inline=True)
            embed.add_field(name="데스카운트", value="10개", inline=True)
            embed.add_field(name="물약 쿨타임", value="5초", inline=True)
            embed.add_field(name="요구 아케인포스", value="360", inline=True)
            embed.add_field(name="페이즈 개수", value="2개", inline=False)
            embed.add_field(name="1페이즈 체력", value="12,000,000,000,000 (12조)", inline=False)
            embed.add_field(name="2페이즈 체력", value="12,000,000,000,000 (12조)", inline=False)
            embed.add_field(name="전체 체력", value="24,000,000,000,000 (24조)", inline=False)
            embed.add_field(name="방어율", value="300%", inline=True)
            embed.add_field(name="파티격 요구스펙",value="[비숍] 220레벨 이상 \n[캐논슈터 등 다수기,타수가 많은 직업] 230레벨 이상 및 무릉 44층 이상, 아케인포스 360 이상 \n[타 직업] 230레벨 이상 및 무릉 45~46층 이상, 아케인포스 360 이상",inline=False)
            embed.add_field(name="솔격 요구스펙", value="[최소컷] 49층 이상 \n[일반컷] 51층 이상", inline=False)
            embed.add_field(name="결정석 가격", value="[본섭] 4061만 2000메소 \n[리부트] 1억 2183만 6000메소", inline=False)
            embed.add_field(name="확정 드랍 보상", value="나비날개 물방울석, \n[본섭] 수상한 에디셔널 큐브 \n[리부트] 장인의 큐브", inline=False)
            embed.add_field(name="확률적 드랍 보상", value="루시드의 소울조각", inline=False)
            embed.add_field(name="공략 영상 URL", value="(추후 추가예정)", inline=False)
            embed.add_field(name="패턴 정보", value="https://namu.wiki/w/루시드(메이플스토리)/보스%20몬스터#s-3", inline=False)
            embed.set_thumbnail(url="https://w.namu.la/s/9af69355d0af6bc2e1fd4284e433090317c1aeb21c43d87658bd071ac759a09971ee9957326e0978d2eef0bbd2ad969566df0f5251327999bd873327562e86eb3b779b34f04fefe2c7c577ba37e6476263fa46b1f5873d400e76438d964d288a")
            await message.channel.send(message.channel, embed=embed)
        elif InputData[1] == "하드루시드" or InputData[1] == "하룻" or InputData[1] == "하루시" or InputData[1] == "하루시드":
            embed = discord.Embed(title="보스몬스터 [하드 루시드] 정보", description="보스몬스터 [하드 루시드]의 정보를 제공해드립니다.", color=0x0000FF)
            embed.add_field(name="입장 요구레벨", value="Lv.220", inline=True)
            embed.add_field(name="몬스터 레벨", value="Lv.230", inline=True)
            embed.add_field(name="제한시간", value="30분 (3페이즈 : 남은 시간과 무관하게 45초)", inline=True)
            embed.add_field(name="데스카운트", value="10개", inline=True)
            embed.add_field(name="물약 쿨타임", value="5초", inline=True)
            embed.add_field(name="요구 아케인포스", value="360", inline=True)
            embed.add_field(name="페이즈 개수", value="2개", inline=False)
            embed.add_field(name="1페이즈 체력", value="41,040,000,000,000 (41조 400억)", inline=False)
            embed.add_field(name="2페이즈 체력", value="41,040,000,000,000 (41조 400억)", inline=False)
            embed.add_field(name="3페이즈 체력", value="11,970,000,000,000 (11조 9700억)", inline=False)
            embed.add_field(name="전체 체력", value="94,050,000,000,000 (94조 500억)", inline=False)
            embed.add_field(name="방어율", value="300%", inline=True)
            embed.add_field(name="파티격 요구스펙",value="[비숍] 220레벨 이상, 프레이 30레벨, 웨폰퍼프-I링 4레벨 이상 보유 및 주스탯 3만 이상 \n[타 직업] 자버프로 230레벨 반감 허수아비 40초딜 1.3~1.4조 이상",inline=False)
            embed.add_field(name="솔격 요구스펙", value="[최소컷] 60층 \n[일반컷] 알려지지 않음", inline=False)
            embed.add_field(name="결정석 가격", value="[본섭] 8800만 메소 \n[리부트] 2억 6400만 메소", inline=False)
            embed.add_field(name="확정 드랍 보상", value="나비날개 물방울석, \n[본섭] 수상한 에디셔널 큐브 \n[리부트] 장인의 큐브", inline=False)
            embed.add_field(name="확률적 드랍 보상", value="루시드의 소울조각, 아케인셰이드 장비, 몽환의 벨트, 루시드로이드", inline=False)
            embed.add_field(name="공략 영상 URL", value="(추후 추가예정)", inline=False)
            embed.add_field(name="패턴 정보", value="https://namu.wiki/w/루시드(메이플스토리)/보스%20몬스터#s-3", inline=False)
            embed.set_thumbnail(url="https://w.namu.la/s/9af69355d0af6bc2e1fd4284e433090317c1aeb21c43d87658bd071ac759a09971ee9957326e0978d2eef0bbd2ad969566df0f5251327999bd873327562e86eb3b779b34f04fefe2c7c577ba37e6476263fa46b1f5873d400e76438d964d288a")
            await message.channel.send(message.channel, embed=embed)
            # 스우
        elif InputData[1] == "스우":
            await message.channel.send('노말 스우와 하드 스우에 대한 정보를 출력합니다.')
            await message.channel.send('&보스정보 노말스우')
            await message.channel.send('&보스정보 하드스우')
            return
        elif InputData[1] == "노말스우" or InputData[1] == "노멀스우" or InputData[1] == "노스우":
            embed = discord.Embed(title="보스몬스터 [노말 스우] 정보", description="보스몬스터 [노말 스우]의 정보를 제공해드립니다.", color=0x0000FF)
            embed.add_field(name="입장 요구레벨", value="Lv.190", inline=True)
            embed.add_field(name="몬스터 레벨", value="Lv.210", inline=True)
            embed.add_field(name="제한시간", value="30분", inline=True)
            embed.add_field(name="데스카운트", value="5개", inline=True)
            embed.add_field(name="물약 쿨타임", value="5초", inline=True)
            embed.add_field(name="페이즈 개수", value="3개", inline=False)
            embed.add_field(name="1페이즈 체력", value="400,000,000,000 (4천억)", inline=False)
            embed.add_field(name="2페이즈 체력", value="400,000,000,000 (4천억)", inline=False)
            embed.add_field(name="3페이즈 체력", value="700,000,000,000 (7천억)", inline=False)
            embed.add_field(name="전체 체력", value="1,500,000,000,000 (1조 5천억)", inline=False)
            embed.add_field(name="방어율", value="300%", inline=True)
            embed.add_field(name="파티격 요구스펙", value="무릉 40층 이상",inline=False)
            embed.add_field(name="솔격 요구스펙", value="[최소컷] 41층 \n[일반컷] 42~3층", inline=False)
            embed.add_field(name="결정석 가격", value="[본섭] 3251만 2500메소 \n[리부트] 9753만 7500메소", inline=False)
            embed.add_field(name="확정 드랍 보상", value="특수형 에너지 코어(S급), 수상한 큐브 \n[본섭] 수상한 에디셔널 큐브 \n[리부트] 장인의 큐브", inline=False)
            embed.add_field(name="확률적 드랍 보상", value="스우의 소울조각", inline=False)
            embed.add_field(name="공략 영상 URL", value="(추후 추가예정)", inline=False)
            embed.add_field(name="패턴 정보", value="https://namu.wiki/w/스우(메이플스토리)/보스%20몬스터#s-3", inline=False)
            embed.set_thumbnail(url="https://ww.namu.la/s/622d50d562fdecb4a0dddb4101fae424f482cb33d588f43965df49da5718e65993bf6222ed27648bb009bbee2b8552687ce30e850c3eeeddaa1837941312b0b38ae326594220b2451312040ca2427720dba7d550a13f2d5e44e5a6363c7f8f52")
            await message.channel.send(message.channel, embed=embed)
        elif InputData[1] == "하드스우" or InputData[1] == "하스우":
            embed = discord.Embed(title="보스몬스터 [하드 스우] 정보", description="보스몬스터 [하드 스우]의 정보를 제공해드립니다.", color=0x0000FF)
            embed.add_field(name="입장 요구레벨", value="Lv.190", inline=True)
            embed.add_field(name="몬스터 레벨", value="Lv.210", inline=True)
            embed.add_field(name="제한시간", value="30분", inline=True)
            embed.add_field(name="데스카운트", value="5개", inline=True)
            embed.add_field(name="물약 쿨타임", value="5초", inline=True)
            embed.add_field(name="페이즈 개수", value="3개", inline=False)
            embed.add_field(name="1페이즈 체력", value="1,400,000,000,000 (1조 4천억)", inline=False)
            embed.add_field(name="2페이즈 체력", value="7,000,000,000,000 (7조)", inline=False)
            embed.add_field(name="3페이즈 체력", value="24,600,000,000,000 (24조 6천억)", inline=False)
            embed.add_field(name="전체 체력", value="33,000,000,000,000 (33조)", inline=False)
            embed.add_field(name="방어율", value="300%", inline=True)
            embed.add_field(name="파티격 요구스펙", value="무릉 50층 이상", inline=False)
            embed.add_field(name="솔격 요구스펙", value="[최소컷] 50층 \n[일반컷] 51~2층", inline=False)
            embed.add_field(name="결정석 가격", value="[본섭] 7411만 2500메소 \n[리부트] 2억 2237만 7500메소", inline=False)
            embed.add_field(name="확정 드랍 보상", value="특수형 에너지 코어(S급), 수상한 큐브 \n[본섭] 수상한 에디셔널 큐브 \n[리부트] 장인의 큐브",inline=False)
            embed.add_field(name="확률적 드랍 보상", value="스우의 소울조각, 손상된 블랙 하트, 앱솔랩스 장비, 루즈 컨트롤 머신 마크", inline=False)
            embed.add_field(name="공략 영상 URL", value="(추후 추가예정)", inline=False)
            embed.add_field(name="패턴 정보", value="https://namu.wiki/w/스우(메이플스토리)/보스%20몬스터#s-3", inline=False)
            embed.set_thumbnail(url="https://ww.namu.la/s/622d50d562fdecb4a0dddb4101fae424f482cb33d588f43965df49da5718e65993bf6222ed27648bb009bbee2b8552687ce30e850c3eeeddaa1837941312b0b38ae326594220b2451312040ca2427720dba7d550a13f2d5e44e5a6363c7f8f52")
            await message.channel.send(message.channel, embed=embed)
        # 데미안
        elif InputData[1] == "데미안":
            await message.channel.send('노말 데미안과 하드 데미안에 대한 정보를 출력합니다.')
            await message.channel.send('&보스정보 노말데미안')
            await message.channel.send('&보스정보 하드데미안')
            return
        elif InputData[1] == "노말데미안" or InputData[1] == "노멀데미안" or InputData[1] == "노데미":
            embed = discord.Embed(title="보스몬스터 [노말 데미안] 정보", description="보스몬스터 [노말 데미안]의 정보를 제공해드립니다.", color=0x0000FF)
            embed.add_field(name="입장 요구레벨", value="Lv.190", inline=True)
            embed.add_field(name="몬스터 레벨", value="Lv.210", inline=True)
            embed.add_field(name="제한시간", value="30분", inline=True)
            embed.add_field(name="데스카운트", value="10개", inline=True)
            embed.add_field(name="물약 쿨타임", value="5초", inline=True)
            embed.add_field(name="페이즈 개수", value="2개", inline=False)
            embed.add_field(name="1페이즈 체력", value="840,000,000,000 (8400억)", inline=False)
            embed.add_field(name="2페이즈 체력", value="360,000,000,000 (3600억)", inline=False)
            embed.add_field(name="전체 체력", value="1,200,000,000,000 (1조 2천억)", inline=False)
            embed.add_field(name="방어율", value="300%", inline=True)
            embed.add_field(name="파티격 요구스펙", value="무릉 40층 이상",inline=False)
            embed.add_field(name="솔격 요구스펙", value="[최소컷] 41층 \n[일반컷] 42~3층", inline=False)
            embed.add_field(name="결정석 가격", value="[본섭] 3380만 0000메소 \n[리부트] 1억 140만 0000메소", inline=False)
            embed.add_field(name="확정 드랍 보상", value="뒤틀린 낙인의 영혼석, 수상한 큐브 \n[본섭] 수상한 에디셔널 큐브 \n[리부트] 장인의 큐브", inline=False)
            embed.add_field(name="확률적 드랍 보상", value="데미안의 소울조각, 루인 포스실드", inline=False)
            embed.add_field(name="공략 영상 URL", value="(추후 추가예정)", inline=False)
            embed.add_field(name="패턴 정보", value="https://namu.wiki/w/데미안(메이플스토리)/보스%20몬스터#s-3", inline=False)
            embed.set_thumbnail(url="https://w.namu.la/s/bf657beb32c44af1ff19915bbe3ea6a8b47b4822a050a9e62cc5c30500da3d4552462a83c822c9ab54cb096ec64c11a72b69164fd21f6bec072cf1c175b114acd6b9da5dd0cfe2702e0d591fefb687406ed11acf1d3b4f1182e3367b8a2bfedd")
            await message.channel.send(message.channel, embed=embed)
        elif InputData[1] == "하드데미안" or InputData[1] == "하데" or InputData[1] == "하데미":
            embed = discord.Embed(title="보스몬스터 [하드 데미안] 정보", description="보스몬스터 [하드 데미안]의 정보를 제공해드립니다.", color=0x0000FF)
            embed.add_field(name="입장 요구레벨", value="Lv.190", inline=True)
            embed.add_field(name="몬스터 레벨", value="Lv.210", inline=True)
            embed.add_field(name="제한시간", value="30분", inline=True)
            embed.add_field(name="데스카운트", value="10개", inline=True)
            embed.add_field(name="물약 쿨타임", value="5초", inline=True)
            embed.add_field(name="페이즈 개수", value="2개", inline=False)
            embed.add_field(name="1페이즈 체력", value="24,850,000,000,000 (24조 8500억)", inline=False)
            embed.add_field(name="2페이즈 체력", value="10,650,000,000,000 (10조 6500억)", inline=False)
            embed.add_field(name="전체 체력", value="35,500,000,000,000 (35조 5000억)", inline=False)
            embed.add_field(name="방어율", value="300%", inline=True)
            embed.add_field(name="파티격 요구스펙", value="무릉 49층 이상", inline=False)
            embed.add_field(name="솔격 요구스펙", value="[최소컷] 53층 \n[일반컷] 알려지지 않음", inline=False)
            embed.add_field(name="결정석 가격", value="[본섭] 7031만 2500메소 \n[리부트] 2억 1093만 7500메소", inline=False)
            embed.add_field(name="확정 드랍 보상", value="뒤틀린 낙인의 영혼석, 수상한 큐브 \n[본섭] 수상한 에디셔널 큐브 \n[리부트] 장인의 큐브",inline=False)
            embed.add_field(name="확률적 드랍 보상", value="데미안의 소울조각, 루인 포스실드, 마력이 깃든 안대, 앱솔랩스 장비", inline=False)
            embed.add_field(name="공략 영상 URL", value="(추후 추가예정)", inline=False)
            embed.add_field(name="패턴 정보", value="https://namu.wiki/w/데미안(메이플스토리)/보스%20몬스터#s-3", inline=False)
            embed.set_thumbnail(url="https://w.namu.la/s/bf657beb32c44af1ff19915bbe3ea6a8b47b4822a050a9e62cc5c30500da3d4552462a83c822c9ab54cb096ec64c11a72b69164fd21f6bec072cf1c175b114acd6b9da5dd0cfe2702e0d591fefb687406ed11acf1d3b4f1182e3367b8a2bfedd")
            await message.channel.send(message.channel, embed=embed)

        # 윌
        elif InputData[1] == "윌" :
            await message.channel.send('노말 윌과 하드 윌에 대한 정보를 출력합니다.')
            await message.channel.send('&보스정보 노말윌')
            await message.channel.send('&보스정보 하드윌')
            return
        elif InputData[1] == "노말윌" or InputData[1] == "노멀윌"  or InputData[1] == "노윌" :
            embed = discord.Embed(title = "보스몬스터 [노말 윌] 정보",description = "보스몬스터 [노말 윌]의 정보를 제공해드립니다.",color = 0x0000FF)
            embed.add_field(name = "입장 요구레벨", value = "Lv.235", inline = True)
            embed.add_field(name = "몬스터 레벨", value = "Lv.250", inline = True)
            embed.add_field(name = "제한시간", value = "30분", inline = True)
            embed.add_field(name = "데스카운트", value = "10개", inline = True)
            embed.add_field(name = "물약 쿨타임", value = "5초 (2페이즈 물약 봉인)", inline = True)
            embed.add_field(name = "요구 아케인포스", value = "760", inline = True)
            embed.add_field(name = "페이즈 개수", value = "3개", inline = False)
            embed.add_field(name = "1페이즈 체력", value = "8,400,000,000,000 (8조 4천억)", inline = False)
            embed.add_field(name = "2페이즈 체력", value = "6,300,000,000,000 (6조 3천억)", inline = False)
            embed.add_field(name = "3페이즈 체력", value = "10,500,000,000,000  (10조 5천억)", inline = False)
            embed.add_field(name = "전체 체력", value = "25,200,000,000,000 (25조 2천억)", inline = False)
            embed.add_field(name = "방어율", value = "300%", inline = True)
            embed.add_field(name = "파티격 요구스펙", value = "[비숍] 235레벨 이상 \n[타 직업] 248레벨 이상 및 무릉 46~7층 이상, 아케인포스 1140 이상", inline = False)
            embed.add_field(name = "솔격 요구스펙", value = "[최소컷] 47층 \n[일반컷] 50층", inline = False)
            embed.add_field(name = "결정석 가격", value = "[본섭] 4651만 2500메소 \n[리부트] 1억 3953만 7500메소", inline = False)
            embed.add_field(name = "확정 드랍 보상", value = "코브웹 물방울석, 수상한 큐브 \n[본섭] 수상한 에디셔널 큐브 \n[리부트] 장인의 큐브", inline = False)
            embed.add_field(name = "확률적 드랍 보상", value = "윌의 소울조각", inline = False)
            embed.add_field(name = "공략 영상 URL", value = "https://www.youtube.com/watch?v=FccQjMzu4fE", inline = False)
            embed.add_field(name = "패턴 정보", value = "https://namu.wiki/w/윌(메이플스토리)/보스%20몬스터#s-4", inline = False)
            embed.set_thumbnail(url = "https://w.namu.la/s/29c4036a996a6bb507664e7a63d78dc7a98aa7a6c03aef579e8378bf73de021318de85ed5eaaa9f1dccd50e4d77298539ca4b5b865da1bc30d4f972c0f03514226aec4a9a3198fd3c7b76b1147e24dd6b8199557cb9c8c4938e86348d54bd208")
            await message.channel.send(message.channel, embed=embed)
        elif InputData[1] == "하드윌" or InputData[1] == "하윌" :
            embed = discord.Embed(title = "보스몬스터 [하드 윌] 정보",description = "보스몬스터 [하드 윌]의 정보를 제공해드립니다.",color = 0x0000FF)
            embed.add_field(name = "입장 요구레벨", value = "Lv.235", inline = True)
            embed.add_field(name = "몬스터 레벨", value = "Lv.250", inline = True)
            embed.add_field(name = "제한시간", value = "30분", inline = True)
            embed.add_field(name = "데스카운트", value = "10개", inline = True)
            embed.add_field(name = "물약 쿨타임", value = "5초 (2페이즈 물약 봉인)", inline = True)
            embed.add_field(name = "요구 아케인포스", value = "760", inline = True)
            embed.add_field(name = "페이즈 개수", value = "3개", inline = False)
            embed.add_field(name = "1페이즈 체력", value = "42,000,000,000,000 (42조)", inline = False)
            embed.add_field(name = "2페이즈 체력", value = "31,500,000,000,000 (31조 5천억)", inline = False)
            embed.add_field(name = "3페이즈 체력", value = "52,500,000,000,000  (52조 5천억)", inline = False)
            embed.add_field(name = "전체 체력", value = "12,600,000,000,000 (126조)", inline = False)
            embed.add_field(name = "방어율", value = "300%", inline = True)
            embed.add_field(name = "파티격 요구스펙", value = "[비숍] 235레벨 이상, 프레이 30레벨, 웨폰퍼프-I링 4레벨 이상 보유 및 주스탯 3만 이상 \n[타 직업] 248레벨 이상 및 무릉 49층 이상, 아케인포스 1140 이상", inline = False)
            embed.add_field(name = "솔격 요구스펙", value = "[최소컷] 61층 \n[일반컷] 알려지지 않음", inline = False)
            embed.add_field(name = "결정석 가격", value = "[본섭] 8820만 메소 \n[리부트] 2억 6460만 메소", inline = False)
            embed.add_field(name = "확정 드랍 보상", value = "코브웹 물방울석, 수상한 큐브, 거울 세계의 코어 젬스톤, \n(최초 격파시) [진실을 꿰뜷는 자] 훈장 \n[본섭] 수상한 에디셔널 큐브 \n[리부트] 장인의 큐브", inline = False)
            embed.add_field(name = "확률적 드랍 보상", value = "윌의 소울조각, 아케인셰이드 장비/방어구, 저주받은 적/청/녹/황의 마도서", inline = False)
            embed.add_field(name = "공략 영상 URL", value = "(추후 영상 첨부)", inline = False)
            embed.add_field(name = "패턴 정보", value = "https://namu.wiki/w/윌(메이플스토리)/보스%20몬스터#s-4", inline = False)
            embed.set_thumbnail(url = "https://w.namu.la/s/29c4036a996a6bb507664e7a63d78dc7a98aa7a6c03aef579e8378bf73de021318de85ed5eaaa9f1dccd50e4d77298539ca4b5b865da1bc30d4f972c0f03514226aec4a9a3198fd3c7b76b1147e24dd6b8199557cb9c8c4938e86348d54bd208")
            await message.channel.send(message.channel, embed=embed)
        # 더스크
        elif InputData[1] == "더스크" or InputData[1] == "거대괴수더스크" :
            await message.channel.send('노말 더스크와 카오스 더스크에 대한 정보를 출력합니다.')
            await message.channel.send('&보스정보 노말더스크')
            await message.channel.send('&보스정보 카오스더스크')
            return
        elif InputData[1] == "노말더스크" or InputData[1] == "노멀더스크" :
            embed = discord.Embed(title = "보스몬스터 [노말 더스크] 정보",description = "보스몬스터 [노말 더스크]의 정보를 제공해드립니다.",color = 0x0000FF)
            embed.add_field(name = "입장 요구레벨", value = "Lv.245", inline = True)
            embed.add_field(name = "몬스터 레벨", value = "Lv.255", inline = True)
            embed.add_field(name = "제한시간", value = "30분", inline = True)
            embed.add_field(name = "데스카운트", value = "5개" , inline = True)
            embed.add_field(name = "물약 쿨타임", value = "5초", inline = True)
            embed.add_field(name = "요구 아케인포스", value = "730", inline = True)
            embed.add_field(name = "페이즈 개수", value = "페이즈로 구분되지 않음", inline = False)
            embed.add_field(name = "전체 체력", value = "26,000,000,000,000 (26조)", inline = False)
            embed.add_field(name = "방어율", value = "300%", inline = True)
            embed.add_field(name = "파티격 요구스펙", value = "50층 이상", inline = False)
            embed.add_field(name = "솔격 요구스펙", value = "[최소컷] 50층 이상 \n[일반컷] 알려지지 않음", inline = False)
            embed.add_field(name = "결정석 가격", value = "[본섭] 4961만 2500메소 \n[리부트] 1억 4883만 7500메소", inline = False)
            embed.add_field(name = "확정 드랍 보상", value = "염원의 불꽃", inline = False)
            embed.add_field(name = "확률적 드랍 보상", value = "없음", inline = False)
            embed.add_field(name = "공략 영상 URL", value = "(추후 영상 첨부)", inline = False)
            embed.add_field(name = "패턴 정보", value = "https://namu.wiki/w/거대%20괴수%20더스크?from=더스크#s-4", inline = False)
            embed.set_thumbnail(url = "https://ww.namu.la/s/7fde8ab44b1723399824fe6dc17fcdeea219d9917c09aa51c5c8ae64062991f75c4aebca9497c9c9b8eec6a74c7ac8366ec37df7f8e731a1769d2c951551f6a98a6cc597a56bb79efed23c40f99e4e097ad852c267cffc64f4b0b5b1d92d7a86")
            await message.channel.send(message.channel, embed=embed)
        elif InputData[1] == "카오스더스크" :
            embed = discord.Embed(title = "보스몬스터 [카오스 더스크] 정보",description = "보스몬스터 [카오스 더스크]의 정보를 제공해드립니다.",color = 0x0000FF)
            embed.add_field(name = "입장 요구레벨", value = "Lv.245", inline = True)
            embed.add_field(name = "몬스터 레벨", value = "Lv.255", inline = True)
            embed.add_field(name = "제한시간", value = "30분", inline = True)
            embed.add_field(name = "데스카운트", value = "5개" , inline = True)
            embed.add_field(name = "물약 쿨타임", value = "5초", inline = True)
            embed.add_field(name = "요구 아케인포스", value = "730", inline = True)
            embed.add_field(name = "페이즈 개수", value = "페이즈로 구분되지 않음", inline = False)
            embed.add_field(name = "전체 체력", value = "114,600,000,000,000 (114조 6000억)", inline = False)
            embed.add_field(name = "방어율", value = "300%", inline = True)
            embed.add_field(name = "파티격 요구스펙", value = "알려지지 않음", inline = False)
            embed.add_field(name = "솔격 요구스펙", value = "[최소컷] 알려지지 않음 \n[일반컷] 알려지지 않음", inline = False)
            embed.add_field(name = "결정석 가격", value = "[본섭] 9245만 메소 \n[리부트] 2억 7735만 메소", inline = False)
            embed.add_field(name = "확정 드랍 보상", value = "염원의 불꽃", inline = False)
            embed.add_field(name = "확률적 드랍 보상", value = "거대한 공포(반지)", inline = False)
            embed.add_field(name = "공략 영상 URL", value = "(추후 영상 첨부)", inline = False)
            embed.add_field(name = "패턴 정보", value = "https://namu.wiki/w/거대%20괴수%20더스크?from=더스크#s-4", inline = False)
            embed.set_thumbnail(url = "https://ww.namu.la/s/7fde8ab44b1723399824fe6dc17fcdeea219d9917c09aa51c5c8ae64062991f75c4aebca9497c9c9b8eec6a74c7ac8366ec37df7f8e731a1769d2c951551f6a98a6cc597a56bb79efed23c40f99e4e097ad852c267cffc64f4b0b5b1d92d7a86")
            await message.channel.send(message.channel, embed=embed)
        # 듄켈
        elif InputData[1] == "듄켈" or InputData[1] == "친위대장듄켈" :
            await message.channel.send('노말 듄켈와 하드 듄켈에 대한 정보를 출력합니다.')
            await message.channel.send('&보스정보 노말듄켈')
            await message.channel.send('&보스정보 하드듄켈')
            return
        elif InputData[1] == "노말듄켈" or InputData[1] == "노멀듄켈" :
            embed = discord.Embed(title = "보스몬스터 [노말 듄켈] 정보",description = "보스몬스터 [노말 듄켈]의 정보를 제공해드립니다.",color = 0x0000FF)
            embed.add_field(name = "입장 요구레벨", value = "Lv.255", inline = True)
            embed.add_field(name = "몬스터 레벨", value = "Lv.265", inline = True)
            embed.add_field(name = "제한시간", value = "30분", inline = True)
            embed.add_field(name = "데스카운트", value = "5개" , inline = True)
            embed.add_field(name = "물약 쿨타임", value = "5초", inline = True)
            embed.add_field(name = "요구 아케인포스", value = "850", inline = True)
            embed.add_field(name = "페이즈 개수", value = "페이즈로 구분되지 않음", inline = False)
            embed.add_field(name = "전체 체력", value = "26,000,000,000,000 (26조)", inline = False)
            embed.add_field(name = "방어율", value = "300%", inline = True)
            embed.add_field(name = "파티격 요구스펙", value = "50층 이상", inline = False)
            embed.add_field(name = "솔격 요구스펙", value = "[최소컷] 52층 이상 \n[일반컷] 알려지지 않음", inline = False)
            embed.add_field(name = "결정석 가격", value = "[본섭] 5281만 2500메소 \n[리부트] 1억 5843만 7500메소", inline = False)
            embed.add_field(name = "확정 드랍 보상", value = "염원의 불꽃", inline = False)
            embed.add_field(name = "확률적 드랍 보상", value = "듄켈의 소울조각", inline = False)
            embed.add_field(name = "공략 영상 URL", value = "(추후 영상 첨부)", inline = False)
            embed.add_field(name = "패턴 정보", value = "https://namu.wiki/w/친위대장%20듄켈?from=듄켈#s-5", inline = False)
            embed.set_thumbnail(url = "https://ww.namu.la/s/43626905051437a851f2fe6763459485f5a9a98cf02ca7923510173a14fec637a4717b44582d8f982b8fa08f0ecece436794e7c5a58f0fcf64cbbbd016bb33aadc906d4623728e21900fc3018b380ef52db658918513a059dec7272b03ff7a1d")
            await message.channel.send(message.channel, embed=embed)
        elif InputData[1] == "하드듄켈" :
            embed = discord.Embed(title = "보스몬스터 [하드 듄켈] 정보",description = "보스몬스터 [하드 듄켈]의 정보를 제공해드립니다.",color = 0x0000FF)
            embed.add_field(name = "입장 요구레벨", value = "Lv.255", inline = True)
            embed.add_field(name = "몬스터 레벨", value = "Lv.265", inline = True)
            embed.add_field(name = "제한시간", value = "30분", inline = True)
            embed.add_field(name = "데스카운트", value = "5개" , inline = True)
            embed.add_field(name = "물약 쿨타임", value = "5초", inline = True)
            embed.add_field(name = "요구 아케인포스", value = "850", inline = True)
            embed.add_field(name = "페이즈 개수", value = "페이즈로 구분되지 않음", inline = False)
            embed.add_field(name = "전체 체력", value = "127,000,000,000,000 (127조)", inline = False)
            embed.add_field(name = "방어율", value = "300%", inline = True)
            embed.add_field(name = "파티격 요구스펙", value = "알려지지 않음", inline = False)
            embed.add_field(name = "솔격 요구스펙", value = "[최소컷] 알려지지 않음 \n[일반컷] 알려지지 않음", inline = False)
            embed.add_field(name = "결정석 가격", value = "[본섭] 9680만 메소 \n[리부트] 2억 9040만 메소", inline = False)
            embed.add_field(name = "확정 드랍 보상", value = "염원의 불꽃", inline = False)
            embed.add_field(name = "확률적 드랍 보상", value = "듄켈의 소울조각, 커맨더 포스 이어링", inline = False)
            embed.add_field(name = "공략 영상 URL", value = "(추후 영상 첨부)", inline = False)
            embed.add_field(name = "패턴 정보", value = "https://namu.wiki/w/친위대장%20듄켈?from=듄켈#s-5", inline = False)
            embed.set_thumbnail(url = "https://ww.namu.la/s/43626905051437a851f2fe6763459485f5a9a98cf02ca7923510173a14fec637a4717b44582d8f982b8fa08f0ecece436794e7c5a58f0fcf64cbbbd016bb33aadc906d4623728e21900fc3018b380ef52db658918513a059dec7272b03ff7a1d")
            await message.channel.send(message.channel, embed=embed)
        # 진 힐라
        elif InputData[1] == "진힐라" or InputData[1] == "하드진힐라" :
            embed = discord.Embed(title = "보스몬스터 [진 힐라] 정보",description = "보스몬스터 [진 힐라]의 정보를 제공해드립니다.",color = 0x0000FF)
            embed.add_field(name = "입장 요구레벨", value = "Lv.250", inline = True)
            embed.add_field(name = "몬스터 레벨", value = "Lv.250", inline = True)
            embed.add_field(name = "제한시간", value = "30분", inline = True)
            embed.add_field(name = "데스카운트", value = "5개 (패턴에 의해 변할 수 있음)", inline = True)
            embed.add_field(name = "물약 쿨타임", value = "5초 (전 페이즈 물약봉인)", inline = True)
            embed.add_field(name = "요구 아케인포스", value = "900", inline = True)
            embed.add_field(name = "페이즈 개수", value = "4개 (구분되지 않음)", inline = False)
            embed.add_field(name = "1페이즈 체력", value = "44,000,000,000,000 (44조)", inline = False)
            embed.add_field(name = "2페이즈 체력", value = "44,000,000,000,000 (44조)", inline = False)
            embed.add_field(name = "3페이즈 체력", value = "44,000,000,000,000 (44조)", inline = False)
            embed.add_field(name = "4페이즈 체력", value = "44,000,000,000,000 (44조)", inline = False)
            embed.add_field(name = "전체 체력", value = "176,000,000,000,000 (176조)", inline = False)
            embed.add_field(name = "방어율", value = "300%", inline = True)
            embed.add_field(name = "파티격 요구스펙", value = "[비숍] 250레벨 이상, 프레이 30레벨, 웨폰퍼프-I링 4레벨 이상 보유 및 주스탯 3.5만 이상 \n[타 직업] 255레벨 이상 및 무릉 52층 이상, 아케인포스 1350 이상", inline = False)
            embed.add_field(name = "솔격 요구스펙", value = "[최소컷] 58층 \n[일반컷] 알려지지 않음", inline = False)
            embed.add_field(name = "결정석 가격", value = "[본섭] 1억 1045만 메소 \n[리부트] 3억 3135만 메소", inline = False)
            embed.add_field(name = "확정 드랍 보상", value = "어두운 힘의 기운, 수상한 큐브 \n[본섭] 수상한 에디셔널 큐브 \n[리부트] 장인의 큐브", inline = False)
            embed.add_field(name = "확률적 드랍 보상", value = "고통의 근원(펜던트), 진 힐라의 소울조각", inline = False)
            embed.add_field(name = "공략 영상 URL", value = "(추후 추가예정)", inline = False)
            embed.add_field(name = "패턴 정보", value = "https://namu.wiki/w/진%20힐라?from=진힐라#s-4", inline = False)
            embed.set_thumbnail(url = "https://ww.namu.la/s/00ce833b6b4c2957e4d6ef7829ec65931e938b7ad5d9106882836b37a41be4c0d8d307c8a07407e53ee9d049539a2fbf1f308d68da7c5d104bcb81a8afce7e9184d486d00ca48f2ee86a68e0280e7333e390503201ca581cd499af2d71ac2ba6")
            await message.channel.send(message.channel, embed=embed)
        # 검은 마법사
        elif InputData[1] == "검은마법사" or InputData[1] == "검마" or InputData[1] == "검맨" or InputData[1] == "하드검은마법사" :
            embed = discord.Embed(title = "보스몬스터 [검은 마법사] 정보",description = "보스몬스터 [검은 마법사]의 정보를 제공해드립니다.",color = 0x0000FF)
            embed.add_field(name = "입장 요구레벨", value = "Lv.255", inline = True)
            embed.add_field(name = "몬스터 레벨", value = "Lv.265", inline = True)
            embed.add_field(name = "제한시간", value = "1시간", inline = True)
            embed.add_field(name = "데스카운트", value = "12개 (패턴에 의해 변할 수 있음)", inline = True)
            embed.add_field(name = "물약 쿨타임", value = "10초", inline = True)
            embed.add_field(name = "요구 아케인포스", value = "1320", inline = True)
            embed.add_field(name = "페이즈 개수", value = "4개", inline = False)
            embed.add_field(name = "1페이즈 체력", value = "65,000,000,000,000 (본체) + 1,000,000,000,000 x n (보호막) (65조 + n조)", inline = False)
            embed.add_field(name = "2페이즈 체력", value = "135,000,000,000,000 (본체) + 1,000,000,000,000 x n (보호막) (135조 + n조)", inline = False)
            embed.add_field(name = "3페이즈 체력", value = "200,000,000,000,000 (본체) + 3,000,000,000,000 x n (보호막) (200조 + 3 x n조)", inline = False)
            embed.add_field(name = "4페이즈 체력", value = "100,000,000,000,000 (본체) + 3,000,000,000,000 x n (보호막) (100조 + 3 x n조)", inline = False)
            embed.add_field(name = "전체 체력", value = "500,000,000,000,000 (본체) + alpha (보호막 체력) (500조 + 보호막 체력)", inline = False)
            embed.add_field(name = "방어율", value = "300%", inline = True)
            embed.add_field(name = "파티격 요구스펙", value = "273레벨 이상 및 무릉 55~56층 이상, 아케인포스 1320 이상", inline = False)
            embed.add_field(name = "솔격 요구스펙", value = "[최소컷] KMS 내 격파자 없음 \n[일반컷] KMS 내 격파자 없음", inline = False)
            embed.add_field(name = "결정석 가격", value = "[본섭] 5억 메소 \n[리부트] 15억 메소", inline = False)
            embed.add_field(name = "확정 드랍 보상", value = "봉인된 제네시스 무기상자, 수상한 큐브 \n[본섭] 수상한 에디셔널 큐브 \n[리부트] 장인의 큐브", inline = False)
            embed.add_field(name = "확률적 드랍 보상", value = "창세의 뱃지", inline = False)
            embed.add_field(name = "공략 영상 URL", value = "(추후 추가예정)", inline = False)
            embed.add_field(name = "패턴 정보", value = "https://namu.wiki/w/검은%20마법사/보스%20몬스터#s-3", inline = False)
            embed.set_thumbnail(url = "https://ww.namu.la/s/dec0777badbae3afa5e0424c2ead2e67184401f5028f5a6339b0ddae14405093a236897d3838d9e7864107ee00fead2753030487691b09435b06f056e7d373054ff34784003cb1f59684c6a29360276fe36c6220d929e633f2606d2696c45329")
            await message.channel.send(message.channel, embed=embed)
        # 선택받은 세렌
        elif InputData[1] == "선택받은세렌" or InputData[1] == "세렌" :
            embed = discord.Embed(title = "보스몬스터 [선택받은 세렌] 정보",description = "보스몬스터 [선택받은 세렌]의 정보를 제공해드립니다.",color = 0x0000FF)
            embed.add_field(name = "입장 요구레벨", value = "Lv.265", inline = True)
            embed.add_field(name = "몬스터 레벨", value = "Lv.275", inline = True)
            embed.add_field(name = "제한시간", value = "30분", inline = True)
            embed.add_field(name = "데스카운트", value = "5개", inline = True)
            embed.add_field(name = "물약 쿨타임", value = "10초", inline = True)
            embed.add_field(name = "요구 어센틱포스", value = "1페이즈: 150 / 2페이즈: 200", inline = True)
            embed.add_field(name = "페이즈 개수", value = "2개(2페이즈 내에서 변동)", inline = False)
            embed.add_field(name = "1페이즈 체력", value = "132,000,000,000,000 (132조)", inline = False)
            embed.add_field(name = "2페이즈 체력", value = "알려지지 않음", inline = False)
            embed.add_field(name = "전체 체력", value = "알려지지 않음", inline = False)
            embed.add_field(name = "방어율", value = "380%", inline = True)
            embed.add_field(name = "파티격 요구스펙", value = "KMS 내 격파자 없음", inline = False)
            embed.add_field(name = "솔격 요구스펙", value = "[최소컷] KMS 내 격파자 없음 \n[일반컷] KMS 내 격파자 없음", inline = False)
            embed.add_field(name = "결정석 가격", value = "[본섭] 5억 메소 \n[리부트] 15억 메소", inline = False)
            embed.add_field(name = "확정 드랍 보상", value = "미트라의 코어 젬스톤, 수상한 큐브 \n[본섭] 수상한 에디셔널 큐브 \n[리부트] 장인의 큐브", inline = False)
            embed.add_field(name = "확률적 드랍 보상", value = "미트라의 분노", inline = False)
            embed.add_field(name = "공략 영상 URL", value = "(추후 추가예정)", inline = False)
            embed.add_field(name = "패턴 정보", value = "https://namu.wiki/w/선택받은%20세렌/공격%20/패턴", inline = False)
            embed.set_thumbnail(url = "https://w.namu.la/s/98698e7995d2511c98b9794b87f414ae147a1706366f14521c703feb0b991b3b501381c5831d6db0faa2bc1a94110c4ba19b7fb027e317e96260fa4371985f18cc3e0f6fc27a8f2265cefe555f1e836a4429546f11a2f695d326de6f5e124d83")
            await message.channel.send(message.channel, embed=embed)
        else :
            await message.channel.send('보스명을 잘못 입력하셨거나 존재하지 않는 보스를 검색하셨습니다. 난이도와 띄어쓰기를 하지 않은 상태로 입력해보세요.')
            return
#버전확인
    elif message.content.startswith('&버전확인'):
        embed = discord.Embed(title="현재 스타포스 시뮬 봇 버전 : 0.1.4.1 (2021.07.06)",description="스타포스 시뮬레이션 봇의 0.1.4.1 버전의 업데이트 내역을 알려드립니다.", color=0x00FF00)
        embed.add_field(name="갱신이 필요한 일부 기능이 6월 내로 수정되거나 삭제됩니다.",value="봇 제작자의 군 입대로 인해 2020/06/08 ~ 2021/12/07 사이 기간동안 주기적인 갱신이 필요한 기능을 유지할 수 없게 되었습니다. 따라서 &로얄 기능과 &매너정보 기능이 삭제되거나 수정될 수 있음을 양해부탁드립니다.", inline=False)
        embed.add_field(name="스타포스 시뮬 봇의 정기점검이 사라집니다.", value="봇 제작자의 군 입대로 인하여 정기점검을 진행할 수 없게 되었습니다. 불편을 끼쳐드려 죄송합니다.")
        embed.add_field(name="도움말의 설명란 내용이 변경됩니다.", value="봇 제작자의 군 입대로 인하여 피드백 등이 불가능함을 공지하는 내용이 추가됩니다.", inline=False)
        embed.add_field(name="스타포스 시뮬레이션 관련 기능의 오류메세지가 추가됩니다.",value="잘못된 입력을 하였을 경우, 정정을 요구하는 답변을 출력하고, 일부 자주 사용되는 기능의 단축 명령어가 추가됩니다.", inline=False)
        embed.add_field(name="스타포스 시뮬 봇의 코드가 개편되었습니다.", value="필요없는 코드가 삭제되어 더 빠른 시뮬레이션이 가능하게 됩니다.", inline=False)
        embed.add_field(name="로얄스타일 목록이 갱신되었습니다.", value="&로얄 (사용갯수) 명령어로 로얄스타일을 시뮬레이션 할 수 있습니다.", inline=False)
        embed.add_field(name="문의", value="다음 URL의 글의 댓글에 문의사항을 작성해주세요. : https://www.blueappleteam.ml/64", inline=False)
        embed.add_field(name="봇 추가 URL",value="https://discordapp.com/oauth2/authorize?client_id=673972036485382168&permissions=67584&scope=bot",inline=False)
        await message.channel.send(message.channel, embed=embed)

#오류반환
    elif message.content.startswith('&'):
        print('Bad request : print help')
        await message.channel.send('명령어를 잊으셨나요? 다시 명령어를 알려드릴게요.')
        await message.channel.send('&도움말')
        print('Request completed') 

#관리용 명령어 모음
    #공지
    if message.content.startswith('%UnstableCode143570132'): await message.channel.send('[공지] 스타포스 시뮬 봇이 패치에 들어가 잠시 불안정해집니다.')
    elif message.content.startswith('%EndCode143570133'):
        embed = discord.Embed(title = "스타포스 시뮬 봇 0.1.4.1 (2021.07.06) 업데이트",description = "스타포스 시뮬레이션 봇의 업데이트가 완료되었습니다.", color = 0x00FF00)
        embed.add_field(name = "스타포스 시뮬레이션이 더 정확해집니다.", value = "기존의 스타캐치 추정치(3%상승)를 수정하여 메이플 공지사항에 게시된 자료(성공확률x1.05)를 반영하였습니다. 이에 따라 기존보다 조금 더 정확한 시뮬레이션이 가능해졌습니다.", inline=False)
        embed.add_field(name = "&보스정보 (보스명) 명령어에 '선택받은 세렌' 보스가 추가되고 오류가 수정됩니다.", value = "&보스정보 (보스명) 입력시 보스몬스터의 사진이 출력되지 않았던 문제를 수정하였고, '선택받은 세렌' 보스를 추가하였습니다.")
        embed.add_field(name = "스타포스 시뮬레이션에 슈페리얼 아이템이 추가됩니다.",value = "&슈페리얼 (세트명) (현재 강화수치) (목표 강화수치) 명령어로 사용할 수 있습니다. 자세한 사항은 &스타포스 명령어를 이용해주시기 바랍니다.", inline = False)
        embed.add_field(name = "&매너정보 (유저명) 기능이 삭제됩니다.",value = "&매너정보 명령어는 데이터의 지속적인 갱신을 요구하며, 다소 주관적인 견해가 반영될 수 있어 부득이하게 삭제하기로 결정하였습니다.", inline = False)
        embed.add_field(name = "스타포스 시뮬 봇의 코드가 개편되었습니다.",value = "필요없는 코드가 삭제되어 더 빠른 시뮬레이션이 가능하게 됩니다.", inline = False)
        embed.add_field(name = "로얄스타일 목록이 갱신되었습니다.", value="&로얄 (사용갯수) 명령어로 로얄스타일을 시뮬레이션 할 수 있습니다.", inline=False)
        embed.add_field(name = "문의",value = "다음 URL의 글의 댓글에 문의사항을 작성해주세요. : https://www.blueappleteam.ml/64", inline = False)
        embed.add_field(name = "봇 추가 URL", value = "https://discordapp.com/oauth2/authorize?client_id=673972036485382168&permissions=67584&scope=bot", inline = False)
        await message.channel.send(message.channel, embed=embed)
    elif message.content.startswith('%CheckVersion'):
        embed = discord.Embed(title = "현재 스타포스 시뮬 봇 버전 : 0.1.4.1 (2021.07.06)",description = "스타포스 시뮬레이션 봇의 0.1.3.4 버전의 업데이트 내역을 알려드립니다.", color = 0x00FF00)
        embed.add_field(name = "갱신이 필요한 일부 기능이 6월 내로 수정되거나 삭제됩니다.", value = "봇 제작자의 군 입대로 인해 2020/06/08 ~ 2021/12/07 사이 기간동안 주기적인 갱신이 필요한 기능을 유지할 수 없게 되었습니다. 따라서 &로얄 기능과 &매너정보 기능이 삭제되거나 수정될 수 있음을 양해부탁드립니다.", inline=False)
        embed.add_field(name = "스타포스 시뮬 봇의 정기점검이 사라집니다.", value = "봇 제작자의 군 입대로 인하여 정기점검을 진행할 수 없게 되었습니다. 불편을 끼쳐드려 죄송합니다.")
        embed.add_field(name = "도움말의 설명란 내용이 변경됩니다.",value = "봇 제작자의 군 입대로 인하여 피드백 등이 불가능함을 공지하는 내용이 추가됩니다.", inline = False)
        embed.add_field(name = "스타포스 시뮬레이션 관련 기능의 오류메세지가 추가됩니다.",value = "잘못된 입력을 하였을 경우, 정정을 요구하는 답변을 출력하고, 일부 자주 사용되는 기능의 단축 명령어가 추가됩니다.", inline = False)
        embed.add_field(name = "스타포스 시뮬 봇의 코드가 개편되었습니다.",value = "필요없는 코드가 삭제되어 더 빠른 시뮬레이션이 가능하게 됩니다.", inline = False)
        embed.add_field(name="로얄스타일 목록이 갱신되었습니다.", value="&로얄 (사용갯수) 명령어로 로얄스타일을 시뮬레이션 할 수 있습니다.", inline=False)
        embed.add_field(name = "문의",value = "다음 URL의 글의 댓글에 문의사항을 작성해주세요. : https://www.blueappleteam.ml/64", inline = False)
        embed.add_field(name = "봇 추가 URL", value = "https://discordapp.com/oauth2/authorize?client_id=673972036485382168&permissions=67584&scope=bot", inline = False)
        await message.channel.send(message.channel, embed=embed)

    #관리
    if message.content.startswith('%CheckServer'):
        list = []
        for server in client.guilds:
            list.append(server.name)
        await message.channel.send("\n".join(list))

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)  #(본섭)

