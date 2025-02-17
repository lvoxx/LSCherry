<p align="center">
  <a href="" rel="noopener">
 <img width="100%" src="https://github.com/lvoxx/LSCherry/blob/main/doc/assets/banner.png" alt="Project Banner"></a>
</p>

<h3 align="center">Toon Shader Library for Blender. Supporting various material processing types for toon rendering.</h3>

<p align="center">
  <a href="#">
    <img alt="GitHub Repo Stars" src="https://img.shields.io/github/stars/lvoxx/LSCherry?style=for-the-badge"/>
  </a>&nbsp;&nbsp;
  <a href="#">
    <img alt="Total Downloads" src="https://img.shields.io/github/downloads/lvoxx/LSCherry/total.svg?style=for-the-badge"/>
  </a>&nbsp;&nbsp;
  <a href="https://www.blender.org/">
    <img alt="Build for Blender" src="https://img.shields.io/badge/blender-%23F5792A.svg?style=for-the-badge&logo=blender&logoColor=white"/>
  </a>&nbsp;&nbsp;
  <a href="https://www.gnu.org/licenses/gpl-3.0">
    <img alt="License: GPL v3" src="https://img.shields.io/badge/License-GPLv3-blue.svg?style=for-the-badge"/>
  </a>&nbsp;&nbsp;
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Prerequisites](#prerequisites)
- [Build-in Toon Support For Games](#build-in)
- [Test File](#tests)
- [User Manual](#user-manual)
- [Creators](#creators)
- [Acknowledgements](#acknowledgements)

## 🧐 About <a name = "about"></a>

Toon Shader for Blender is inspired by <a href="[doc:intro-to-readme](https://www.youtube.com/@aVersionOfReality)">aVersionOfReality</a> and is a library designed to be compatible with many contemporary anime-style games and pure toon aesthetics. The basic configurations have been pre-set up and integrated with toolsets to facilitate connections with other similar or compatible toon libraries.

## 🏁 Getting Started <a name = "getting_started"></a>

1. Download and extract the release.</br>
![Screenshot (1928)](https://github.com/lvoxx/LSCherry/assets/95278222/70f1f18d-e45b-4170-bb76-4a3624c13d27)

2. Add Asset Library In File Path
* Note: You can use LSCherry as a local asset (Append) to share your work with others or lock down the LSCherry version you prefer.</br>
![Screenshot 2024-04-14 110334](https://github.com/lvoxx/LSCherry/assets/95278222/d4f1b22d-8d16-4bb8-aa53-a80401b54be5)

3. Open Asset Browser and drag object "Cherry".</br>
<img src="https://github.com/lvoxx/LSCherry/assets/95278222/faf729cc-0408-4f43-883f-c76cceaea012"/>

4. Open Shader Editor and find "Make Toon" node and connect it to Material Output.</br>
<img src="https://github.com/lvoxx/LSCherry/assets/95278222/63153287-1603-483c-ab79-98228fdb34b6"/>


5. Yes, its done ✨🎉🎉. If you want to use additional features or pre-built packages, please search for nodes within the materials present in the LSCherry object or those prefixed with "Game Name". Example: HI3, GI, HSR,... find more prefix at [Build-in Toon Support For Games](#build-in)

## ❗ Prerequisites <a name = "prerequisites"></a>

### 🛠️ Blender version should be **3.x.x** or **4.x.x**
### 🛠️ The LSCherry nodes link to the scr, make sure to relink the source or local it all
⚠️ Blender version **2.x.x** or **older** will cause unexpected issues ⚠️

| Require name          | Description                  | Where To Download                                                                                  | Is |
| --------------------- | ---------------------------- | -------------------------------------------------------------------------------------------------- | :-----: |
| Blender               | For LSCherry                 | <a href="https://www.blender.org/download/">Download</a>                                           |   Required    |
| Auto Reload Libraries | Auto reload linked libraries | <a href="https://github.com/lvoxx/LSCherry/blob/main/addon/auto_reload_libraries.zip">Download</a> |   Required    |
| VF PlanarUV           | For Frequent Hair Highlight  | <a href="https://github.com/lvoxx/LSCherry/blob/main/addon/VF_planarUV.py">Download</a>            |   Optional    |
| Mesh Fairing Master   | Quick Clean Shading Face     | <a href="https://github.com/lvoxx/LSCherry/blob/main/addon/mesh-fairing-master.zip">Download</a>   |   Optional    |

## 📦 Build-in Toon Support For Games <a name = "build-in"></a>

| Package               | Build-in Support | Prefix |
| --------------------- | :--------------: | :----: |
| Honkai Impact 3       |        ✔️        |  HI3   |
| Genshin Impact        |        ✔️        |   GI   |
| Zenless Zone Zero     |        ❌        |  ZZZ   |
| Honkai Starrail       |        ✔️        |  HSR   |
| Punishing: Gray Raven |        ❌        |  PGR   |
| Girls Frontline 2     |        ❌        |  GF2   |
| Persona Series        |        ❌        |  PSN   |
| Wuthering Waves       |        ❌        |   WW   |
| Aether Gazer          |        ❌        |   AG   |
| Project Snow          |        ❌        |  PJS   |

## 🔧 Tests File <a name = "tests"></a>

Check out test file using build-in packages.
[Go To Tests](https://github.com/lvoxx/LSCherry/tree/main/test)

### Honkai Impact 3
<strong>Elysia</strong></br>
<img src="https://github.com/lvoxx/LSCherry/assets/95278222/2801a4a4-3923-4fb1-bdae-f279fa876f15" width = "350"/>

<strong>Vill-V</strong></br>
<img src="https://github.com/lvoxx/LSCherry/assets/95278222/90f2ef91-2cc2-48c9-a346-5418d9ec9585" width = "350"/>


## 📖 User Manual <a name = "user-manual"></a>

Check for guild lines in my repos wiki</br>
[Go To Wiki](https://github.com/lvoxx/LSCherry/wiki)

## ✍️ Creators <a name = "creators"></a>

Respect for those who have created wonderful addons and library.

|                                                                                                                                         Author                                                                                                                                          |                                                                                                                                          Auto Reload Libraries                                                                                                                                          |                                                                                                                                            VF PlanarUV                                                                                                                                            |                                                                                                                                 Mesh Fairing Master                                                                                                                                 |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [<img src="https://github.com/lvoxx.png?size=250" width=115><br><sub>@lvoxx</sub>](https://github.com/lvoxx) <br><br> [![Github-sponsors](https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AAA)](https://www.patreon.com/lvoxxArtist) | [<img src="https://github.com/gandalf3.png?size=250" width=115><br><sub>@gandalf3</sub>](https://github.com/gandalf3) <br><br> [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/gandalf3/auto-reload-linked-libraries) | [<img src="https://github.com/jeinselen.png?size=250" width=115><br><sub>@jeinselen</sub>](https://github.com/jeinselen) <br><br> [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/jeinselen/VF-BlenderPlanarUV) | [<img src="https://github.com/fedackb.png?size=250" width=115><br><sub>@fedackb</sub>](https://github.com/fedackb) <br><br> [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/fedackb/mesh-fairing) |

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

|                                                                                                                                                                     Inspiration by<br>aVersionOfReality                                                                                                                                                                     |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [<img src="https://yt3.googleusercontent.com/3eV9mOZaAJ9Uh16gMaiq8pXwPe9lVlk-K3UR4pkzZ3ggKT7zA-ZZ8GlUqjsvfy6vmIRbURlq=s160-c-k-c0x00ffffff-no-rj" width=115><br>](https://www.youtube.com/@aVersionOfReality)<br> [![Youtube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@aVersionOfReality) |

### References

Not update yet.
