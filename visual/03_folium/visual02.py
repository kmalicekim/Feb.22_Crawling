import folium

my_loc = folium.Map(location=[37.50355897410302, 127.04977599773379], zoom_start=18)
folium.Marker([37.50355897410302, 127.04977599773379], popup=folium.Popup('멀티캠퍼스 선릉', max_width=100)).add_to(my_loc)

my_loc.save('visual02.html')

# 척도 (zoom_start)의 min/max 값
# marker 만든것 my_loc 추가해야지 -> add_to