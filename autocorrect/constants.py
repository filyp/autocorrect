# -*- coding: utf-8 -*-

word_regexes = {
    'en': r'[A-Za-z]+',
    'pl': r'[A-Za-zęĘóÓąĄśŚłŁżŻźŹćĆńŃ]+',
    'ru': r'[АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя]+',
    'uk': r'[АаБбВвГгҐґДдЕеЄєЖжЗзИиІіЇїЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬЮюЯя]+',
    'tr': r'[a-zA-ZçÇğĞüÜöÖşŞıİ]+',
    'es': r'[A-Za-zÁáÉéÍíÓóÚúÜüÑñ]+',
}

alphabets = {
    'en': 'abcdefghijklmnopqrstuvwxyz',
    'pl': 'abcdefghijklmnopqrstuvwxyzęóąśłżźćń',
    'ru': 'шиюынжсяплзухтвкйеобмцьёгдщэарчфъ',
    'uk': 'фагксщроємшплуьцнжхїйювязтибґідеч',
    'tr': 'abcçdefgğhıijklmnoöprsştuüvyzqwxÇĞİÜÖ',
    'es': 'abcdefghijklmnopqrstuvwxyzáéíóúüñ',
}

urls = {
    'en': 'https://drive.google.com/uc?export=download&id=19xqFyk9d8mFR7LR43oy6cExk8Pk9wVwV',
    'pl': 'https://drive.google.com/uc?export=download&id=1kqGWZLUsE8YAB-_nvfMJXNTjYBsjIvSN',
    'ru': 'https://drive.google.com/uc?export=download&id=1vvOako2MwtexEHX24Jx5CjjN-1yEXOrf',
    'uk': 'https://drive.google.com/uc?export=download&id=1nG_DG6aWU1PUA_DPSfrvh92puTLr8-aA',
    'tr': 'https://drive.google.com/uc?export=download&id=1ZGQEhLTteTQprRpnKrHTFWeV2RxYny21',
    'es': 'https://drive.google.com/uc?export=download&id=19VQuOE12sb0p10SBKWRbSdnUvk0eeFPg',
}
