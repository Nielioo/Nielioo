from datetime import datetime

with open("./README.md", "w") as f:
    f.write(f'''![cheers](https://github.com/Nielioo/Nielioo/blob/main/Assets/XinyanCheer.gif)
![guitar](https://github.com/Nielioo/Nielioo/blob/main/Assets/XinyanGuitar.gif)
![cheers](https://github.com/Nielioo/Nielioo/blob/main/Assets/XinyanCheer.gif)
![guitar](https://github.com/Nielioo/Nielioo/blob/main/Assets/XinyanGuitar.gif)
![cheers](https://github.com/Nielioo/Nielioo/blob/main/Assets/XinyanCheer.gif)
![guitar](https://github.com/Nielioo/Nielioo/blob/main/Assets/XinyanGuitar.gif)

Updated: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
''')