import pandas as pd
d = {'name': pd.Series(['Гиперион', 'Менара в долине Данум', 'Центурион', 'Прибрежная пихта Дугласа', 'Ель ситкинская', 'Самая высокая гигантская секвойя в бассейне реки Конверс', 'Кипарис у залива Лангдра Ней', 'Сэр Вим (Один из белых рыцарей)', 'Эвкалипт шаровидный', ' Эвкалипт косой']),
     'lat': pd.Series(['Hyperion', 'Menara in Danum Valle', 'Centurio', 'Douglas Abies Maritima', 'Sitkin Abiegnis', 'sequoia gigas longissimi In Lacu Fluminis Converso', 'Cupressus apud Langdra Ney Bay', ' Domine Wim (Unus E Militibus Albis)', 'eucalyptus globulus', 'Eucalyptus obliquus']),
     'size': pd.Series([115.85, 100.8, 99.82, 99.75, 96.7, 95.8, 94.6, 91.3, 90.7, 88])}
s=pd.DataFrame(d)
s.to_csv('res.csv')
print(s)

