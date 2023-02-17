from pbt.translations import *


ts = TranslationSet()

ts.append(T(tag="ClumpLabel/text",
    text='COMP')
    .es(1)
    .pt(1)
    .fr(1)
    .it(0)
    .ja('コンプ')
    .ko('컴프')
    .zhHans('压缩')
    .zhHant('壓縮')
    .ar('الضغط')
    .he('קומפרשן')
)

ts.append(T(tag="ClumpLabel/text",
    text='COMP ADV')
    .es('COMP EXT')
    .pt('COMP +')
    .fr('COMP EXT')
    .it(0)
    .ja('コンプ詳細設定')
    .ko('세부 컴프레션 조절')
    .zhHans('高级压缩设定')
    .zhHant('進階動態設定')
    .ar('+ الضغط')
    .he('קומפרשן ועוד')
)

ts.append(T(tag="ClumpLabel/text",
    text='IN')
    .es('ENTRADA')
    .pt('ENTRADA')
    .fr('ENTRÉE')
    .it(0)
    .ja('イン')
    .ko('인풋')
    .zhHans('输入')
    .zhHant('輸入')
    .ar('دَخْل')
    .he('כניסה')
)

ts.append(T(tag="ClumpLabel/text",
    text='LOFI')
    .es(1)
    .pt(1)
    .fr(1)
    .it(0)
    .ja('ローファイ')
    .ko('로우파이')
    .zhHans('低保真度')
    .zhHant('低傳真度')
    .ar('اللٌُوفَاي')
    .he('לו-פיי')
)

ts.append(T(tag="ClumpLabel/text",
    text='LOFI ADV')
    .es('LOFI EXT')
    .pt('LOFI +')
    .fr('LOFI EXT')
    .it(0)
    .ja('ローファイ詳細設定')
    .ko('세부 로우파이 조절')
    .zhHans('高级低保真设定')
    .zhHant('進階低傳真度設定')
    .ar('+ اللٌُوفَاي')
    .he('לו-פיי ועוד')
)

ts.append(T(tag="ClumpLabel/text",
    text='OUT')
    .es('SALIDA')
    .pt('SAÍDA')
    .fr('SORTIE')
    .it(0)
    .ja('アウト')
    .ko('아웃풋')
    .zhHans('输出')
    .zhHant('輸出')
    .ar('خَرْج')
    .he('יציאה')
)

ts.append(T(tag="ClumpLabel/text",
    text="""
        SIDE
        CHAIN""")
    .es(1)
    .pt(1)
    .fr(1)
    .it(0)
    .ja("""
        サイド
        チェイン""")
    .ko("""
        사이드
        체인""")
    .zhHans('旁链')
    .zhHant('旁鏈')
    .ar("""
        شين
        السايد""")
    .he('סייד-צ׳יין')
)

ts.append(T(tag="ClumpLabel/text",
    text='WOW')
    .es(1)
    .pt(1)
    .fr(1)
    .it(0)
    .ja('ワウ')
    .ko('와우')
    .zhHans('抖晃')
    .zhHant('抖晃')
    .ar('الواو')
    .he('ואוו')
)

ts.append(T(tag="ClumpLabel/text",
    text='WOW ADV')
    .es('WOW EXT')
    .pt('WOW +')
    .fr('WOW EXT')
    .it(0)
    .ja('ワウ詳細設定')
    .ko('세부 와우 조절')
    .zhHans('高级抖晃低')
    .zhHant('進階抖晃設定')
    .ar('+ الواو')
    .he('ואוו ועוד')
)

ts.append(T(tag="ClumpLabel/text",
    text='dry')
    .es(1)
    .pt(1)
    .fr(1)
    .it(0)
    .ja('原音')
    .ko('원음')
    .zhHans('干声')
    .zhHant('乾聲')
    .ar('جاف')
    .he('מיקס')
)

ts.append(T(tag="ParamLabel/text",
    text='Attack')
    .es('Ataque')
    .pt('Ataque')
    .fr('Attaque')
    .it(0)
    .ja('アタック')
    .ko('어택')
    .zhHans('起动时间')
    .zhHant('起動時間')
    .ar('زمن التطبيق')
    .he('זמן התקף')
)

ts.append(T(tag="ParamLabel/text",
    text='Crunch')
    .es(1)
    .pt('Crocância')
    .fr(1)
    .it(0)
    .ja('クランチ')
    .ko('크런치')
    .zhHans('摩擦声')
    .zhHant('摩擦聲')
    .ar('القرمَشة')
    .he('קראנצ׳')
)

ts.append(T(tag="ParamLabel/text",
    text='Digital Ref Level')
    .es('Nivel de referencia digital')
    .pt('Nível de Referência Digital')
    .fr('Niveau de Référence Digital')
    .it(0)
    .ja('デジタルリファレンスレベル')
    .ko('디지털 레퍼런스 레벨')
    .zhHans('数字参考电平')
    .zhHant('數位參考電平')
    .ar('مستوى المَرْجِع الرقمي')
    .he('רפרנס דיגיטלי')
)

ts.append(T(tag="ParamLabel/text",
    text='External Sidechain')
    .es('Sidechain externo')
    .pt('Sidechain Externo')
    .fr('Sidechain Externe')
    .it(0)
    .ja('外部サイドチェイン')
    .ko('외부 사이드체인')
    .zhHans('外部旁链')
    .zhHant('外部旁鏈')
    .ar('سايدشين خارجي')
    .he('סייד-צ׳יין חיצוני')
)

ts.append(T(tag="ParamLabel/text",
    text='Mix')
    .es('Mezcla')
    .pt(1)
    .fr(1)
    .it(0)
    .ja('ミックス')
    .ko('믹스')
    .zhHans('混合')
    .zhHant('混合')
    .ar('الميكس')
    .he('מיקס')
)

ts.append(T(tag="ParamLabel/text",
    text='Noise')
    .es('Ruido')
    .pt('Ruído')
    .fr('Bruit')
    .it(0)
    .ja('ノイズ')
    .ko('노이즈')
    .zhHans('噪声')
    .zhHant('雜訊')
    .ar('الضجيج')
    .he('רעש')
)

ts.append(T(tag="ParamLabel/text",
    text='Phase')
    .es('Fase')
    .pt('Fase')
    .fr(1)
    .it(0)
    .ja('フェイズ')
    .ko('페이즈')
    .zhHans('相位')
    .zhHant('相位')
    .ar('الطور')
    .he('פאזה')
)

ts.append(T(tag="ParamLabel/text",
    text='Release')
    .es('Relajación')
    .pt('Repouso')
    .fr('Retour')
    .it(0)
    .ja('リリース')
    .ko('릴리즈')
    .zhHans('释放时间')
    .zhHant('釋放時間')
    .ar('التحرير')
    .he('זמן שחרור')
)

ts.append(T(tag="ParamLabel/text",
    text='Sidechain Tilt')
    .es('Inclinación del Sidechain')
    .pt('Inclinação do Sidechain')
    .fr('Inclinaison du Sidechain')
    .it(0)
    .ja('サイドチェインチルト')
    .ko('사이드체인 틸트')
    .zhHans('旁链倾斜')
    .zhHant('旁鏈傾斜')
    .ar('إمالةُ السايدشين')
    .he('סייד-צ׳יין טילט')
)

ts.append(T(tag="ParamLabel/text",
    text='Speed')
    .es('Velocidad')
    .pt('Velocidade')
    .fr('Vitesse')
    .it(0)
    .ja('RPM')
    .ko('RPM')
    .zhHans('速度')
    .zhHant('速度')
    .ar('السرعة')
    .he('מהירות')
)

ts.append(T(tag="ParamLabel/text",
    text='Stereo Link')
    .es('Link estéreo')
    .pt('Link Estéreo')
    .fr('Couplage Stéréo')
    .it(0)
    .ja('ステレオリンク')
    .ko('스테레오 링크')
    .zhHans('双声道连结')
    .zhHant('雙聲道連結')
    .ar('الوصل إستيريو')
    .he('קישור סטריאו')
)

ts.append(T(tag="ParamLabel/text",
    text='Type')
    .es('Tipo')
    .pt('Tipo')
    .fr(1)
    .it(0)
    .ja('タイプ')
    .ko('유형')
    .zhHans('类型')
    .zhHant('類型')
    .ar('النوع')
    .he('סוג')
)

ts.append(T(tag="Parameter/option",
    context="LoFiType",
    text="1980's Digital")
    .es('Digital: 1980s')
    .pt('Digital: Anos 80')
    .fr('Digital Années 80')
    .it(0)
    .ja('80年代デジタル')
    .ko('80년대 디지털')
    .zhHans('1980数位')
    .zhHant('1980數位')
    .ar('رقمي: سنوات ال80')
    .he('אייטיז דיגיטל')
)

ts.append(T(tag="Parameter/option",
    context="LoFiType",
    text="1990's Digital")
    .es('Digital: 1990s')
    .pt('Digital: Anos 90')
    .fr('Digital Années 90')
    .it(0)
    .ja('90年代デジタル')
    .ko('90년대 디지털')
    .zhHans('1990数位')
    .zhHant('1990數位')
    .ar('رقمي: سنوات ال90')
    .he('ניינטיז דיגיטל')
)

ts.append(T(tag="Parameter/option",
    context="LoFiType",
    text='Analog')
    .es('Análogo')
    .pt('Analógico')
    .fr('Analogique')
    .it(0)
    .ja('アナログ')
    .ko('아날로그')
    .zhHans('模拟')
    .zhHant('類比')
    .ar('أنالوج')
    .he('אנלוג')
)

ts.append(T(tag="Tagline",
    text='Beastly compression, by Vulf')
    .es('Compresión feroz, al estilo Vulf')
    .pt('Compressão monstruosa, no estilo Vulf')
    .fr('Compression de monstre, par Vulf')
    .it(0)
    .ja('強烈なエンボスを作成\u3000ビースティ・コンプレッサー by Vulf')
    .ko('Vulf 스타일의 강렬한 컴프레션')
    .zhHans('野兽般强而有力的压缩')
    .zhHant('野獸般強而有力的壓縮')
    .ar('Vulf ضغط وَحْشِيّ، بواسطة')
    .he('קומפרסיה מפלצתית וולף סטייל')
)

