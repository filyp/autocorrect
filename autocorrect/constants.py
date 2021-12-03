word_regexes = {
    "en": r"[A-Za-z]+",
    "pl": r"[A-Za-zęĘóÓąĄśŚłŁżŻźŹćĆńŃ]+",
    "ru": r"[АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя]+",
    "uk": r"[АаБбВвГгҐґДдЕеЄєЖжЗзИиІіЇїЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬЮюЯя]+",
    "tr": r"[a-zA-ZçÇğĞüÜöÖşŞıİ]+",
    "es": r"[A-Za-zÁáÉéÍíÓóÚúÜüÑñ]+",
    "pt": r"[a-zA-ZãáàâçéêíõóôúüÃÁÀÂÇÉÊÍÕÓÔÚÜ]+",
    "cs": r"[AÁBCČDĎEÉĚFGH(Ch)IÍJKLMNŇOÓPQRŘSŠTŤUÚŮVWXYÝZŽaábcčdďeéěfgh(ch)iíjklmnňoópqrřsštťuúůvwxyýzž]+",
    "el": r"[α-ωΑ-ΩίϊΐόάέύϋΰήώΊΪΪ́ΌΆΈΎΫΫ́ΉΏ]+",
    "it": r"[a-zA-ZãáàâçéêíõóôúüÃÁÀÂÇÉÊÍÕÓÔÚÜ]+",
    "fr": r"[a-zA-ZãáàâçéêíõóôúüÃÁÀÂÇÉÊÍÕÓÔÚÜ]+",
    "vi": r"[a-zA-ZàáạảãÀÁẠẢÃằắặẳẵẰẮẶẲẴầấậẩẫẦẤẬẨẪèéẹẻẽÈÉẸẺẼềếệểễỀẾỆỂỄìíịỉĩÌÍỊỈĨòóọỏõÒÓỌỎÕồốộổỗỒỐỘỔỖờớợởỡỜỚỢỞỠùúụủũÙÚỤỦŨừứựửữỪỨỰỬỮỳýỵỷỹỲÝỴỶỸ]+",
}

alphabets = {
    "en": "abcdefghijklmnopqrstuvwxyz",
    "pl": "abcdefghijklmnopqrstuvwxyzęóąśłżźćń",
    "ru": "шиюынжсяплзухтвкйеобмцьёгдщэарчфъ",
    "uk": "фагксщроємшплуьцнжхїйювязтибґідеч",
    "tr": "abcçdefgğhıijklmnoöprsştuüvyzqwxÇĞİÜÖ",
    "es": "abcdefghijklmnopqrstuvwxyzáéíóúüñ",
    "pt": "abcdefghijklmnopqrstuvwxyzãáàâçéêíõóôúü",
    "cs": "aábcčdďeéěfgh(ch)iíjklmnňoópqrřsštťuúůvwxyýzž",
    "el": "αβγδεζηθικλμνξοπρςτυφχψωίϊΐόάέύϋΰήώ",
    "it": "abcdefghijklmnopqrstuvwxzyãáàâçéêíõóôúü",
    "fr": "abcdefghijklmnopqrstuvwxzyãáàâçéêíõóôúü",
    "vi": "aàảãáạăằẳẵắặâầẩẫấậbcdđeèẻẽéẹêềểễếệfghiìỉĩíịjklmnoòỏõóọôồổỗốộơờởỡớợpqrstuùủũúụưừửữứựvwxyỳỷỹýỵz",
}

ipfs_gateways = [
    "http://ipfs.io/ipfs/",
    "https://gateway.pinata.cloud/ipfs/",
    # this one has the best performance, but doesn't return download progress
    "https://cf-ipfs.com/ipfs/",
]

ipfs_paths = {
    "en": ["QmbRSZvfJV6zN12zzWhecphcvE9ZBeQdAJGQ9c9ttJXzcg/en.tar.gz"],
    "pl": ["QmbRSZvfJV6zN12zzWhecphcvE9ZBeQdAJGQ9c9ttJXzcg/pl.tar.gz"],
    "ru": ["QmbRSZvfJV6zN12zzWhecphcvE9ZBeQdAJGQ9c9ttJXzcg/ru.tar.gz"],
    "uk": ["QmbRSZvfJV6zN12zzWhecphcvE9ZBeQdAJGQ9c9ttJXzcg/uk.tar.gz"],
    "tr": ["QmbRSZvfJV6zN12zzWhecphcvE9ZBeQdAJGQ9c9ttJXzcg/tr.tar.gz"],
    "es": ["QmbRSZvfJV6zN12zzWhecphcvE9ZBeQdAJGQ9c9ttJXzcg/es.tar.gz"],
    "cs": ["QmbRSZvfJV6zN12zzWhecphcvE9ZBeQdAJGQ9c9ttJXzcg/cs.tar.gz"],
    "pt": ["QmbRSZvfJV6zN12zzWhecphcvE9ZBeQdAJGQ9c9ttJXzcg/pt.tar.gz"],
    "el": ["QmbRSZvfJV6zN12zzWhecphcvE9ZBeQdAJGQ9c9ttJXzcg/el.tar.gz"],
    "it": ["QmbRSZvfJV6zN12zzWhecphcvE9ZBeQdAJGQ9c9ttJXzcg/it.tar.gz"],
    "fr": ["QmPRNDmUDTXikq8gWnGcw3ZGmnoBfvekmAyeyX8y6onf23/fr.tar.gz"],
    "vi": ["QmRRJj5i7nkpzTRSKhFe23XMjLRw7f2zD6FLKDrRfzco7f/vi.tar.gz"],
}

backup_urls = {
    "en": [
        "https://dl.dropboxusercontent.com/s/grxjmtw4db814g1/en.tar.gz?dl=0",
    ],
    "pl": [
        "https://dl.dropboxusercontent.com/s/40orabi1l3dfqpp/pl.tar.gz?dl=0",
    ],
    "ru": [
        "https://dl.dropboxusercontent.com/s/mpas7xqn8yl3wej/ru.tar.gz?dl=0",
        "https://dl.dropboxusercontent.com/s/6tzfxy34xx34mm7/ru.tar.gz?dl=0",
    ],
    "uk": [
        "https://dl.dropboxusercontent.com/s/s64ot0l4lj3a0ec/uk.tar.gz?dl=0",
        "https://dl.dropboxusercontent.com/s/b76p4sc1lld96lw/uk.tar.gz?dl=0",
    ],
    "tr": [
        "https://dl.dropboxusercontent.com/s/mj2d3t158ucwhwx/tr.tar.gz?dl=0",
        "https://dl.dropboxusercontent.com/s/1wy01nq5fpq8iay/tr.tar.gz?dl=0",
    ],
    "es": [
        "https://dl.dropboxusercontent.com/s/jh0212sou1qbs7t/es.tar.gz?dl=0",
        "https://dl.dropboxusercontent.com/s/k6g5vj3x0rx7mjz/es.tar.gz?dl=0",
    ],
    "cs": [
        "https://dl.dropboxusercontent.com/s/8ptuuh8kcr3kufy/cs.tar.gz?dl=0",
        "https://dl.dropboxusercontent.com/s/369wplqb0w2ax21/cs.tar.gz?dl=0",
    ],
    "pt": [
        "https://dl.dropboxusercontent.com/s/6xnko882tsjgeaw/pt.tar.gz?dl=0",
    ],
    "el": [
        "https://dl.dropboxusercontent.com/s/2zdewe1p1od9vu0/el.tar.gz?dl=0",
    ],
    "it": [
        "https://dl.dropboxusercontent.com/s/6xci1wfb387zk23/it.tar.gz?dl=0",
    ],
    "fr": ["https://mega.nz/file/kQByQJAb#rMbmF0HG09MLQQ-FDafHrPAgXigJIpmC1zhtxRMp2dQ"],
}
