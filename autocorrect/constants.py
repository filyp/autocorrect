word_regexes = {
    'en': r'[A-Za-z]+',
    'pl': r'[A-Za-zęĘóÓąĄśŚłŁżŻźŹćĆńŃ]+',
    'ru': r'[АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя]+',
    'uk': r'[АаБбВвГгҐґДдЕеЄєЖжЗзИиІіЇїЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬЮюЯя]+',
    'tr': r'[a-zA-ZçÇğĞüÜöÖşŞıİ]+',
    'es': r'[A-Za-zÁáÉéÍíÓóÚúÜüÑñ]+',
    'cs': r'[AÁBCČDĎEÉĚFGH(Ch)IÍJKLMNŇOÓPQRŘSŠTŤUÚŮVWXYÝZŽaábcčdďeéěfgh(ch)iíjklmnňoópqrřsštťuúůvwxyýzž]+',
}

alphabets = {
    'en': 'abcdefghijklmnopqrstuvwxyz',
    'pl': 'abcdefghijklmnopqrstuvwxyzęóąśłżźćń',
    'ru': 'шиюынжсяплзухтвкйеобмцьёгдщэарчфъ',
    'uk': 'фагксщроємшплуьцнжхїйювязтибґідеч',
    'tr': 'abcçdefgğhıijklmnoöprsştuüvyzqwxÇĞİÜÖ',
    'es': 'abcdefghijklmnopqrstuvwxyzáéíóúüñ',
    'cs': 'aábcčdďeéěfgh(ch)iíjklmnňoópqrřsštťuúůvwxyýzž',
}

# urls = {
#     'en': 'https://drive.google.com/uc?export=download&id=19xqFyk9d8mFR7LR43oy6cExk8Pk9wVwV',
#     'pl': 'https://drive.google.com/uc?export=download&id=1kqGWZLUsE8YAB-_nvfMJXNTjYBsjIvSN',
#     'ru': 'https://drive.google.com/uc?export=download&id=1vvOako2MwtexEHX24Jx5CjjN-1yEXOrf',
#     'uk': 'https://drive.google.com/uc?export=download&id=1nG_DG6aWU1PUA_DPSfrvh92puTLr8-aA',
#     'tr': 'https://drive.google.com/uc?export=download&id=1ZGQEhLTteTQprRpnKrHTFWeV2RxYny21',
#     'es': 'https://drive.google.com/uc?export=download&id=19VQuOE12sb0p10SBKWRbSdnUvk0eeFPg',
# }

urls = {
    'en': [
        'https://dl.dropboxusercontent.com/s/jyyuqrtcbusw1kq/en.tar.gz?dl=0',
        'https://dl.dropboxusercontent.com/s/cz6koxli82rqdia/en.tar.gz?dl=0',
        'https://siasky.net/_AqMToyBioTOgKzTHwCsurBfeOwq4XGbV38ryEXwR_ULQA',],
    'pl': [
        'https://dl.dropboxusercontent.com/s/7izndbb0buoufcg/pl.tar.gz?dl=0',
        'https://dl.dropboxusercontent.com/s/3nfolvuz7clzuz4/pl.tar.gz?dl=0',
        'https://siasky.net/AAC52kUAAmfZF_DUZVMQWWO-tJ3g3_3FDEhR2BUXr4oq8Q',],
    'ru': [
        'https://dl.dropboxusercontent.com/s/mpas7xqn8yl3wej/ru.tar.gz?dl=0',
        'https://dl.dropboxusercontent.com/s/6tzfxy34xx34mm7/ru.tar.gz?dl=0',
        'https://siasky.net/AABaSQMcxgHp7LJ-YHs1IWqn4uxa8q17fGET-IaNbGgSnQ',],
    'uk': [
        'https://dl.dropboxusercontent.com/s/s64ot0l4lj3a0ec/uk.tar.gz?dl=0',
        'https://dl.dropboxusercontent.com/s/b76p4sc1lld96lw/uk.tar.gz?dl=0',
        'https://siasky.net/AADdpauxvMwjieU3n5qaMbjAeCYR9T-vK6L1OEXRTOgr6g',],
    'tr': [
        'https://dl.dropboxusercontent.com/s/mj2d3t158ucwhwx/tr.tar.gz?dl=0',
        'https://dl.dropboxusercontent.com/s/1wy01nq5fpq8iay/tr.tar.gz?dl=0',
        'https://siasky.net/AABWRhJ-7NVoo2vaTgSs6HNhwGmFgCgYzg0q_0d-eqgCeA',],
    'es': [
        'https://dl.dropboxusercontent.com/s/jh0212sou1qbs7t/es.tar.gz?dl=0',
        'https://dl.dropboxusercontent.com/s/k6g5vj3x0rx7mjz/es.tar.gz?dl=0',
        'https://siasky.net/_ArsYbh-vpFWosvzEuQQZnPrOt2XggjDQfkvDwTFu5MQoA',],
    'cs': [
        'https://dl.dropboxusercontent.com/s/8ptuuh8kcr3kufy/cs.tar.gz?dl=0',
        'https://dl.dropboxusercontent.com/s/369wplqb0w2ax21/cs.tar.gz?dl=0',
        'https://siasky.net/AAC6lW1ShlSRUeiFnr4_2bmw6sznlZsWvmhDhyQy_-g2wA',],
}
