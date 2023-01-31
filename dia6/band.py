from instruments import EletricGuitar, Flute, Guitar, DisortionKind


gianini = Guitar("Giannini m2")
print(gianini.play())
print(gianini.colors)


yamaha = Flute("Ymaha Magic Flute")
print(yamaha.play())
print(yamaha.colors)


leaspaul = EletricGuitar("lespaul m1")
print(leaspaul.play(distorcion=DisortionKind.whisper))
print(leaspaul.play(distorcion=DisortionKind.wave))
