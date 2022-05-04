void main(List<String> args) {
  var isimler = <String>[
    "Arda",
    "Berk",
    "Buğra",
    "Muhammed",
    "Yalçın",
    "Serdar"
  ];

  Yonetici.uyeEkle(isimler);

  Yonetici yonetici1 = Yonetici("Admin", "12");
  print(Uye.uyeler);
  yonetici1.aidatOde();
  yonetici1.aidatEkle(2, 200);
  print(yonetici1.bilgiGoruntule(2));
  print(yonetici1);
}

class Uye {
  static List<Uye> uyeler = [];
  String isim;
  String daire;
  double? aidat;

  Uye(this.isim, this.daire);

  void aidatOde() {
    print("Aidat Ödendi");
  }

  @override
  String toString() {
    return "Üye ismi: $isim daire numarası: $daire bu ayki aidatı: ${aidat ?? "mevcut değil"} ";
  }
}

class Yonetici extends Uye {
  Yonetici(String isim, String daire) : super(isim, daire);

  void aidatEkle(int daireNo, double aidat) {
    Uye.uyeler[daireNo - 1].aidat = aidat;
  }

  Uye bilgiGoruntule(int daireNo) {
    return Uye.uyeler[daireNo - 1];
  }

  static void uyeEkle(List<String> isimler) {
    for (int i = 0; i < isimler.length; i++) {
      Uye.uyeler.add(Uye(isimler[i], (i + 1).toString()));
    }
  }
}
