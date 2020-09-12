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
    'cs': 'aábcčdďeéěfgh(ch)iíjklmnňoópqrřsštťuúůvwxyýzž.',
}

urls = {
    'en': 'https://dl.dropboxusercontent.com/s/cz6koxli82rqdia/en.tar.gz?dl=0',
    'pl': 'https://dl.dropboxusercontent.com/s/3nfolvuz7clzuz4/pl.tar.gz?dl=0',
    'ru': 'https://dl.dropboxusercontent.com/s/6tzfxy34xx34mm7/ru.tar.gz?dl=0',
    'uk': 'https://dl.dropboxusercontent.com/s/b76p4sc1lld96lw/uk.tar.gz?dl=0',
    'tr': 'https://dl.dropboxusercontent.com/s/1wy01nq5fpq8iay/tr.tar.gz?dl=0',
    'es': 'https://dl.dropboxusercontent.com/s/k6g5vj3x0rx7mjz/es.tar.gz?dl=0',
    'cs': 'https://dl.dropboxusercontent.com/s/369wplqb0w2ax21/cs.tar.gz?dl=0',
}
