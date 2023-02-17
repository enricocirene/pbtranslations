from pbt.translations import *


ts = TranslationSet()

ts.append(T(tag="ClumpLabel/text",
    text='LIM/SAT')
    .es(1)
    .pt(1)
    .fr(1)
    .it(0)
    .ja("""
        リミッター /
        サチュレーター""")
    .ko("""
        리미터 /
        세츄레이터""")
    .zhHans("""
        限制／
        饱和设定""")
    .zhHant("""
        限制／
        飽和設定""")
    .ar(1)
    .he('לימ׳/סאט׳')
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
    .ar('الخرج')
    .he('יציאה')
)

ts.append(T(tag="ParamLabel/text",
    text='Color')
    .es('Coloración')
    .pt('Coloração')
    .fr('Coloration')
    .it(0)
    .ja('カラー')
    .ko('컬러')
    .zhHans('染色')
    .zhHant('染色')
    .ar('اللّون')
    .he('צבע')
)

ts.append(T(tag="ParamLabel/text",
    text='DRY')
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
    text="""
        Filter
        Glide Time""")
    .es("""
        Tiempo de
        Barrido de Filtro""")
    .pt("""
        Tempo de
        Glide do Filtro""")
    .fr("""
        Temps de
        Balayage du Filtre""")
    .it(0)
    .ja("""
        フィルター
        グライド""")
    .ko("""
        필터
        글라이드""")
    .zhHans("""
        滤波
        滑移时间""")
    .zhHant("""
        濾波
        滑移時間""")
    .ar("""
        توقيت انزلاق
        الفلتر""")
    .he('זמן שחרור פילטר')
)

ts.append(T(tag="ParamLabel/text",
    text='Frequency')
    .es('Frecuencia')
    .pt('Frequência')
    .fr('Fréquence')
    .it(0)
    .ja('周波数')
    .ko('필터 기준 주파수')
    .zhHans('频率')
    .zhHant('頻率')
    .ar('التردد')
    .he('תדר')
)

ts.append(T(tag="ParamLabel/text",
    text="""
        Lim/Sat
        Auto Gain""")
    .es("""
        Ganancia Auto.
        Lim./Sat.""")
    .pt("""
        Compensar Ganho
        Lim/Sat""")
    .fr("""
        Lim/Sat
        Gain Automatique""")
    .it(0)
    .ja("""
        Lim/Sat
        オートゲイン""")
    .ko("""
        Lim/Sat
        오토 게인""")
    .zhHans("""
        限制器/饱和器
        自动增益""")
    .zhHant("""
        限制器/飽和器
        自動增益""")
    .ar("""
        الربح التلقائي
        Lim/Satلل""")
    .he("""
        גיין אוטומטי
        לימ׳/סאט׳""")
)

ts.append(T(tag="ParamLabel/text",
    text="""
        Lim/Sat
        Stereo Link""")
    .es("""
        Vínculo Estéreo
        Lim./Sat.""")
    .pt("""
        Link Estéreo
        Lim/Sat""")
    .fr("""
        Lim/Sat
        Couplage Stéréo""")
    .it(0)
    .ja("""
        Lim/Sat
        ステレオリンク""")
    .ko("""
        Lim/Sat
        스테레오 링크""")
    .zhHans("""
        限制器/饱和器
        立体声连结""")
    .zhHant("""
        限制器/飽和器
        立體聲連結""")
    .ar("""
        وصل الإستيرِو
        Lim/Satلل""")
    .he("""
        קישור סטריאו
        לימ׳/סאט׳""")
)

ts.append(T(tag="ParamLabel/text",
    text='Mix')
    .es('Mezcla')
    .pt(1)
    .fr(1)
    .it(0)
    .ja('ミックス')
    .ko('필터 믹스')
    .zhHans('混合')
    .zhHant('混合')
    .ar('الميكس')
    .he('מיקס')
)

ts.append(T(tag="ParamLabel/text",
    text='Resonance')
    .es('Resonancia')
    .pt('Ressonância')
    .fr('Résonance')
    .it(0)
    .ja('レゾナンス')
    .ko('필터 레조넌스')
    .zhHans('共振')
    .zhHant('共振')
    .ar('الرنين')
    .he('רזוננס')
)

ts.append(T(tag="ParamLabel/text",
    text='Slope')
    .es('Pendiente')
    .pt('Declive')
    .fr('Ordre')
    .it(0)
    .ja('スロープ')
    .ko('필터 기울기')
    .zhHans('坡度')
    .zhHant('坡度')
    .ar('الميل')
    .he('מדרון')
)

ts.append(T(tag="ParamLabel/text",
    text='Threshold')
    .es('Umbral')
    .pt('Limite')
    .fr('Seuil')
    .it(0)
    .ja('スレッショルド')
    .ko('기준 레벨')
    .zhHans('阈值')
    .zhHant('閾值')
    .ar('حد العتبة')
    .he('סף')
)

ts.append(T(tag="Tagline",
    text='Filter sweeps: lo, hi, & anywhere in between')
    .es('Barridos de filtro: altos, bajos y entre medio')
    .pt('Varreduras de filtro: grave, agudo e tudo que há no meio')
    .fr("Balayages de filtres: bas, haut, et tout l'entre-deux")
    .it(0)
    .ja('極細繊維で紡いだ6.0dB~96dBのフィルター')
    .ko('자유로운 필터 스윕')
    .zhHans('全能滤波器：任何频段、全能控制')
    .zhHant('全能濾波器：任何頻段、全能控制')
    .ar('عمليّة مسح الفِلترات:منخفضة، عالية و في أيّ مكان فيما بين')
    .he('פילטר סוויפס: נמוכים, גבוהים וכל מה שביניהם')
)

