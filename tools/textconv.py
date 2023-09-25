# -*- coding: utf-8 -*-
import sys

fontset_jp = [
"あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんがぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽぁぃぅぇぉっゃゅょアイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワンガギグゲゴザジズゼゾダヂヅデドバビブベボヴパピプペポァィゥェォッャュョー0123456789０１２３４５６７８９、。！？・「」（）∼～　⑫ ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ，一二三四五六七八九＋十Ｇ．ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳ",
"ＴＵＶＷＸＹＺ½④⅛①♥▼ヲ　¼②¼¼¼神何会賊大男元気出状今皇帝聖寺恩勇者苦加争攻撃力守備魔竜石団閾技場店必殺道読杖系星話兵士使用運速法軍白火飛地暗黒進城海人騎院王子女様父行戦来母山集剣国待祖老東方辺境小援助両親討身愛妹姫才々？年日対岸街彼解放島南北西近村旅悪知陸草原建以他土占領狼名弟半公数月前主破同盟内財宝敵箱俺奴中央路下都谷築無砦最将指揮唯門始後退入休養税金自治好意的傭久喜持願質捕要塞決罠言見性恐思上悲辛分代救率末千宮物多達目市家統合事世黙種武器挑血筋貴陰独立偉手痛敗向農水緑美",
"荒迎全部隊取罪賢光殿阻止英雄強背隣未開族切従現弱復活受猛誇滅亡古高度絶動塔司祭失追込包囲所突散残選命巣歩盗巻心着生足移文明望時平和支配激界秘野乱域帯難開打倒死槍弓斧民位先利兄氷信真正義忠誠臣婚礼廷伯伝説炎紋章景反爵枢卿侯断記録初写消第町隷天空駆遠征連去嘆紅峡墓謎再奪回落帰還壇制圧病終編相商勝負続素示賞椨然異壊護熱譏各装妹安貨侵玉座準鉄銀屋百封印盾電問橋併脱防壮冷昔途宮黄狂志希重栄発歴語味体令精鋭邪恊拇完政緒節砂漠灼太陽当党本能少作幸理新夫逃略不永参惨減成共訪誘感与挟長具坦急由",
"耳産招視超仲変務償売買声教恋員服修屈注巨情徒馬森得機軽経験昇格扱有若涙効特殊離存在呪仕御興蛮化外抵抗処刑掃陛獄可個室形択引控旗密林掘設赤短乗卑劣友逆派遣拠踊迷宿勉学伐福限議営被果保害期埋溶岩別想像雲眠凍肌転陣崩衛息類脈実憶非術郊鋼維承談遺増磨活孤児風結尽諸浪複否定留戻請流側任僧侶称号念忘涯妻災頼姿甲申遊委貯良弔漁師捨雑託娘告赴予裂努燎役仮面暮我堂腕輩導業創史績敬応計了暖現模報皆払混双口降伏改革幅侮悔毎牢虜肉到却妃倍迫求職魂紙標通供許局送絡孫扉約束万左右峠闇稼嫁走台握宣覇唱怒咸",
"付頃盛衰徴低牙没鈍細拓勃川募陥呼起誕権泣欲河音返段階功況頭歯車式檄寸深纖筈酷私囚君造訳組授誓早郎固我手品挙総危猟雇寄顔捜等裹為働預謀犬吠容態置腹次勢深刻図朝葉延覚悟怪巻丈影腰抜序舞誰獅刃霊巫首片貨聞険住柄昼楽係借甥荷閉善積晴証益困逝確責満惜渉交泥条憎答調価値犠牲誉裔直抱居招労押簡案傷砕至隠認易幼端育線己哀契優雅毒差厚更叩画障使罰広顧属暦虐宰狩油舌吟詩掟拡里拍駐維問題過番帚汚胎謝慕奇跡赦蜂額展恥孝肩雷禁管臨投周単矢儀弾床拒覧富歓群凱旋鳥春雪典毛根旧余温姪基練微笑湖妙試躍快婦冗木",
"芸糸衣感庶咲花清尊因夜甘弁汁誤件校例"]

fontset_kr = [
"!?,~().아다지하어가는그고도니라을나리의에요은해로스게만기서시님들자있마를네으야르한세군신겠까거제없말드트내주면무전부왕안습었대저수버여정우보너것건알와인께래당데려할성난레미않실디람란했상되놈러모돌바생죽렇터금후국런공비용머선크과좋냐힘음걸프명뭐테싸진두았분방단운위같워함던죠키적각반히치때더벨싶럼린발간셨조샤응살예장희못합계토ー0123456789、。！？・「」（）∼ABCDEFGHIJKLMNOPQRSTUVWXYZ，일이삼사오육칠팔구십Ｇ．ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳ",
"ＴＵＶＷＸＹＺ④①♥직　②⑫⑩1C=⑩②⑤⑧②동잘소율줄든랑움심온피입노원경물받누행격남켜갈날중슬된번됐망쟁걱탁검엘빠녀줘빈속필설왔돼감길딘강처잖황문손폐져따브언렌역찮괜였파겐막유베불약왜울떻슨끝작배력죄느참렸애호름질페겨통목티샨앞찾쳐태될많결릴병법뿐석송긴봐암큭훗얼친재족쪽화출타헤맡쓸임흑연올졌둘령체코럴잡투활달짓차귀며카눈식넌답째큐론숨슈줬혼곁순잊교민잠준겁맞복쓰곧른볼승억락록앗영쩔패혀흥별빨케평끌절믿싫압텍났본산셔텐관떠먼몰몸밖씀잉끼침형얘천클듯룸잃즐렉씨열좀추항끄윽청허회갔빛뻐엔젠",
"집험또년떨립먹백붙퓨괴럽롭루매쉬핀환꼭냥딸랬빼외윈점포갑깨벌젊창쿠틸편확늘듣악척훌곳략링새젤책킬향뜨맹밀혹흐렙렴뭔개낼널능닌륭몇웠최큰궁뇨돈랜충품견놓땐랐례멸쩌표협곤근넘닫멋봤깐놀떤변빌쁜찬탈튜휘힐꾸맙멍북써큼광꿈닥증갖굴늦땅뜻림멜옆즈찌쳤탄팡풀급담뒤엇짜튼완잔존즉닙덕돕듀딤랄쫓춤커꼴둠똑뢰뭘뻔양얻착현꺼넣녕농뒷련뭣밌쌍왠쯤철낌높놔됩둔둬메박숲옛옥접채취특픈혜휴겼깊둑둥득멈뭉쁘엄촌츠틀핑획흘꿔납냈닮델뛰륙멀벗색익잭켰튀헛굳글껏꽃닐등렵뱀봉술쉽앙종택퍼딱렀류맥밝숙웃짐쳇초픔홀골",
"귄끔낸늙랍삶섬셀슴킴톡틈풍플핫힌갚꺄끊낳롱뤼벡셈쇠씻앵짝축쿨펜헌혈흔권꼬끈닿덤듭랫럭료솔웅쥐즘쭉챙첫춰탓턴판학흰김깃껜냉덧렁범섭쌓쏟쓴씬액업엽엾윤졸쩍쭈총칫칭탑퇴혔곱꾼딛렛뤄릅릇맛맨묻블싼썩앉얌옷욕욱잇쩡측칼흉갓껴눠댁댄덴독딜뚫렬맺몫봬뵙빚뻤섯센셋쇼씌얍얕엉엣염옮옵짖쨌찍췄컷켁콜킨팀펠펼훨흠갇값걔겔겸굉궤규긍껄꼽꽤꾀꿀꿉꿍낄낡낮녁념뇌눌덜땠떼띄랭량룩룬룰륜릿맘묘묵밑밥뱅벼빴뿔삐섞섰솜솟쏙엑젓좌쥬짧쩜찢찰춘춥칙컬쾌탐탤폭혐효훔휩걷겝겪괘굶궂귐균극긁긋깜깥꺾꼐꽉꿨꿰뀌끓낀낙낫냅넋",
"넓넙녔녹논눴뉘닉닝닦댈덟덮뎌뒀딪딴땀땄떡뚱뜬뜯뜸랏럿롯릎맑멘멩몹묶뭇뭡밟밤밴뱃벤벽봄뵌붓붕빕뺄뻗뽑뿌쁩샌샐섣섹셜숍숭쉴쌈쑤씁씩씸앓얄얽엠엥엮엿옙옹욘윌젖죗줍짊징짼쩐쫑쭐찔찻챘첨첩칩컸콘콤콱퀸탬템텨톰톱틱틴팽펑펴풋핏햇헉헬홈횡힝깝웬벅똘월컴",
""]

def get_fontset(n):
    r = -1
    for ff in fontset_kr:
        r += 1
        p = ff.find(n)
        if p != -1:
            return r
    r = -1
    for ff in fontset_jp:
        r += 1
        p = ff.find(n)
        if p != -1:
            return r
    return -1



file = open(sys.argv[1], "r", encoding="UTF8")
output = open(sys.argv[2], "w", encoding="UTF8")
while True:
    line = file.readline()
    fontset_n = -1
    if not line:
        break
    
    line2 = line.lstrip()
    sp = line2.find(' ')
    sp2 = line2.find('.')
    if sp == -1 and len(line2) > 0:
        fontset_n = -1
    if sp != -1:
        opp = line2[:sp]
        if opp == '.stringn' :
            leftpos = len(line)-len(line2)
            leftText = line[:leftpos]
            mainText = line2[(sp+1):].rstrip()
            iA = 0
            iB = False
            
            
            tT = ""

            for i in range(0, len(mainText)):
                
                if iB == True:
                    tT += "\\" + mainText[i]
                    iB = False
                elif mainText[i] == "\"":
                    if(iA == 0):
                        iA+=1
                    next
                elif mainText[i] == "\\":
                    iB = True
                    next
                else:
                    iC = get_fontset(mainText[i])
                    if (iC < 0):
                        print("unregistered char:"+mainText[i])
                    if(iC == fontset_n):
                        tT += mainText[i]
                        next
                    else:
                        if tT != "":
                            output.write(leftText + ".stringn \"" + tT + "\"" +"\n")
                        output.write(leftText + "db Font%d" % (iC+1) +"\n")
                        fontset_n = iC
                        tT = mainText[i]
                    #
                #
            output.write(leftText + ".stringn \"" + tT + "\""+"\n")
        else:
            output.write(line.rstrip()+"\n")
    else:
        output.write(line.rstrip()+"\n")
file.close()


