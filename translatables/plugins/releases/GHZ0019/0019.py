from pbt.translations import *


ts = TranslationSet()

ts.append(T(tag="Parameter/option",
    context="TempoMode",
    text='BPM Sync')
    .es('BPM Sinc')
    .pt('BPM Sinc')
    .fr(1)
    .it('BPM Sinc')
    .ja('BPMシンク')
    .ko('BPM 싱크')
    .zhHans('BPM同步')
    .zhHant('BPM同步')
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="TempoMode",
    text='BPM Free')
    .es(0)
    .pt(0)
    .fr('BPM Libre')
    .it(0)
    .ja('BPMフリー')
    .ko(0)
    .zhHans(0)
    .zhHant(0)
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="TempoMode",
    text='MS')
    .es(1)
    .pt(1)
    .fr(1)
    .it(1)
    .ja(1)
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="AInputMode",
    text='Left')
    .es('Izquierda')
    .pt('Esquerda')
    .fr('Gauche')
    .it('Sinistra')
    .ja('左')
    .ko('좌')
    .zhHans('左')
    .zhHant('左')
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="AInputMode",
    text='Right')
    .es('Derecha')
    .pt('Direita')
    .fr('Droite')
    .it('Destra')
    .ja('右')
    .ko('우')
    .zhHans('右')
    .zhHant('右')
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="AInputMode",
    text='Sum')
    .es(0)
    .pt(0)
    .fr('Somme')
    .it(0)
    .ja('合計')
    .ko(0)
    .zhHans(0)
    .zhHant(0)
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="BInputMode",
    text='Right')
    .es('Derecha')
    .pt('Direita')
    .fr('Droite')
    .it('Destra')
    .ja('右')
    .ko('우')
    .zhHans('右')
    .zhHant('右')
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="BInputMode",
    text='Left')
    .es('Izquierda')
    .pt('Esquerda')
    .fr('Gauche')
    .it('Sinistra')
    .ja('左')
    .ko('좌')
    .zhHans('左')
    .zhHant('左')
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="BInputMode",
    text='Sum')
    .es(0)
    .pt(0)
    .fr('Somme')
    .it(0)
    .ja('合計')
    .ko(0)
    .zhHans(0)
    .zhHant(0)
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="GlideMode",
    text='Relative')
    .es('Relativo')
    .pt('Relativo')
    .fr('Relatif')
    .it('Relativo')
    .ja('相対的')
    .ko('상대적')
    .zhHans('相对的')
    .zhHant('相對的')
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="GlideMode",
    text='Absolute')
    .es('Absoluto')
    .pt('Absoluto')
    .fr('Absolu')
    .it('Assoluto')
    .ja('絶対的')
    .ko('절대적')
    .zhHans('绝对的')
    .zhHant('絕對的')
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="SpringDecayMode",
    text='Auto')
    .es('Automático')
    .pt('Automático')
    .fr('Automatique')
    .it('Automatico')
    .ja('自動')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    context="SpringDecayMode",
    text='Manual')
    .es(1)
    .pt(1)
    .fr('Manuel')
    .it('Manuale')
    .ja('手動')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar(0)
    .he(0)
)

ts.append(T(tag="Tagline",
    text='A weird little delay concept')
    .es(0)
    .pt(0)
    .fr('Un petit concept de delay hors norme')
    .it(0)
    .ja('少し変わったディレイコンセプト')
    .ko(0)
    .zhHans(0)
    .zhHant(0)
    .ar(0)
    .he(0)
)

ts.append(T(tag="ClumpLabel/text",
    text='SYNC')
    .es('SINC')
    .pt('SINC')
    .fr(1)
    .it('SINC')
    .ja('シンク')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar(0)
    .he(0)
)

ts.append(T(tag="ClumpLabel/text",
    text='Free')
    .es(0)
    .pt(0)
    .fr('Libre')
    .it(0)
    .ja('フリー')
    .ko(0)
    .zhHans(0)
    .zhHant(0)
    .ar(0)
    .he(0)
)

ts.append(T(tag="ParamLabel/bgtext",
    text='Spring')
    .es(0)
    .pt(0)
    .fr('Ressort')
    .it(0)
    .ja('スプリング', vertical=True)
    .ko(0)
    .zhHans(0)
    .zhHant(0)
    .ar(0)
    .he(0)
)

ts.append(T(tag="ParamLabel/bgtext",
    text='Feedback')
    .es(0)
    .pt(0)
    .fr(1)
    .it(0)
    .ja('フィードバック', vertical=True)
    .ko(0)
    .zhHans(0)
    .zhHant(0)
    .ar(0)
    .he(0)
)

ts.append(T(tag="ParamLabel/bgtext",
    text='Output')
    .es('Salida')
    .pt('Saída')
    .fr('Sortie')
    .it('Uscita')
    .ja('アウトプット', vertical=True)
    .ko('아웃풋')
    .zhHans('输出')
    .zhHant('輸出')
    .ar(0)
    .he(0)
)

ts.append(T(tag="ParamLabel/text",
    text='Mix')
    .es('Mezcla')
    .pt(1)
    .fr(1)
    .it('Miscela')
    .ja('ミックス')
    .ko('필터 믹스')
    .zhHans('混合')
    .zhHant('混合')
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    text='Kill All')
    .es(0)
    .pt(0)
    .fr('Arrêt Complet')
    .it(0)
    .ja('全て停止')
    .ko(0)
    .zhHans(0)
    .zhHant(0)
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    text='Kill Feedback')
    .es(0)
    .pt(0)
    .fr('Arrêt Feedback')
    .it(0)
    .ja('フィードバック停止')
    .ko(0)
    .zhHans(0)
    .zhHant(0)
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    text='Infinite Hold')
    .es(0)
    .pt(0)
    .fr('Hold Infini')
    .it(0)
    .ja('無限ホールド')
    .ko(0)
    .zhHans(0)
    .zhHant(0)
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    text='Spring Hold')
    .es(0)
    .pt(0)
    .fr('Hold Ressort')
    .it(0)
    .ja('スプリングホールド')
    .ko(0)
    .zhHans(0)
    .zhHant(0)
    .ar(0)
    .he(0)
)

ts.append(T(tag="ParamLabel/text",
    text='Tape')
    .es('Cinta')
    .pt(1)
    .fr(1)
    .it('Nastro')
    .ja('テープ')
    .ko('테이프')
    .zhHans('磁带')
    .zhHant('磁帶')
    .ar(0)
    .he(0)
)

ts.append(T(tag="ParamLabel/text",
    text='Lofi')
    .es(1)
    .pt(1)
    .fr(1)
    .it(1)
    .ja('ローファイ')
    .ko('로우파이')
    .zhHans('低保真度')
    .zhHant('低傳真度')
    .ar(0)
    .he(0)
)

ts.append(T(tag="ParamLabel/text",
    text='Wobble')
    .es(0)
    .pt(0)
    .fr('Oscill')
    .it(0)
    .ja('ぐらぐら')
    .ko(0)
    .zhHans(0)
    .zhHant(0)
    .ar(0)
    .he(0)
)

ts.append(T(tag="ParamLabel/text",
    text='Filter')
    .es('Filtro')
    .pt('Filtro')
    .fr('Filtre')
    .it('Filtro')
    .ja('フィルター')
    .ko('필터')
    .zhHans('滤波')
    .zhHant('濾波')
    .ar(0)
    .he(0)
)

ts.append(T(tag="ParamLabel/text",
    text='Freq')
    .es('Frec')
    .pt(1)
    .fr('Fréq')
    .it(1)
    .ja('周波数')
    .ko('프리퀀시')
    .zhHans('频率')
    .zhHant('頻率')
    .ar(0)
    .he(0)
)

ts.append(T(tag="ParamLabel/text",
    text='Binaural')
    .es(0)
    .pt(0)
    .fr(1)
    .it(0)
    .ja('バイノーラル')
    .ko(0)
    .zhHans(0)
    .zhHant(0)
    .ar(0)
    .he(0)
)

ts.append(T(tag="ParamLabel/text",
    text='Spread')
    .es(0)
    .pt(0)
    .fr('Diffusion')
    .it(0)
    .ja('スプレッド')
    .ko(0)
    .zhHans(0)
    .zhHant(0)
    .ar(0)
    .he(0)
)

ts.append(T(tag="ParamLabel/text",
    text='Glide')
    .es('Barrido')
    .pt(1)
    .fr('Balayage')
    .it('Attraversamento')
    .ja('グライド')
    .ko('글라이드')
    .zhHans('滑移')
    .zhHant('滑移')
    .ar(0)
    .he(0)
)

ts.append(T(tag="ParamLabel/text",
    text='Time')
    .es('Tiempo')
    .pt('Tempo')
    .fr('Temps')
    .it('Tempo')
    .ja('時間')
    .ko(1)
    .zhHans(1)
    .zhHant(1)
    .ar(0)
    .he(0)
)

ts.append(T(tag="ParamLabel/text",
    text='Spring')
    .es(0)
    .pt(0)
    .fr('Ressort')
    .it(0)
    .ja('スプリング')
    .ko(0)
    .zhHans(0)
    .zhHant(0)
    .ar(0)
    .he(0)
)

ts.append(T(tag="ParamLabel/text",
    text='Decay')
    .es('Decai')
    .pt('Decai')
    .fr(1)
    .it('Declino')
    .ja('ディケイ')
    .ko('디케이')
    .zhHans('衰减')
    .zhHant('衰減')
    .ar(0)
    .he(0)
)

ts.append(T(tag="Parameter/option",
    text='+DRY')
    .es(1)
    .pt(1)
    .fr(1)
    .it('+ORIG')
    .ja('＋原音')
    .ko('+원음')
    .zhHans('+干声')
    .zhHant('+乾聲')
    .ar(0)
    .he(0)
)

