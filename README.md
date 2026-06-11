<p align="center">
  <a href="" rel="noopener">
    <img width="60%" src="https://github.com/lvoxx/LSCherry/blob/main/doc/assets/banner.png?raw=1" alt="Project Banner">
  </a>
</p>

<h3 align="center">Toon Shader Framework for Blender. Supporting various material processing types for toon rendering.</h3>

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

Toon Shader for Blender and GooEngine is inspired by <a href="https://www.youtube.com/@aVersionOfReality">aVersionOfReality</a> and is a framework designed to be compatible with many contemporary anime-style games and pure toon techniques. The basic configurations have been pre-set up and integrated with LSPotato addon to facilitate connections with other similar or compatible toon stlyzes.<br/>

> [!NOTE]  
> Follow project updates on **[Discord Forum](https://discord.com/channels/894925535870865498/1229033388946755734)**

## ❗ Prerequisites <a name = "prerequisites"></a>

> [!IMPORTANT]
> 🛠️ Blender version should be **4.x.x** or **5.x.x**. </br>
> The LSCherry nodes link to the scr, make sure to relink the source or local it all

> [!WARNING]
> Blender version **3.x.x** or **older** will cause unexpected issues or crashing.

| Require name          | Description                  | Where To Download                                                                                  |    Is    |
| --------------------- | ---------------------------- | -------------------------------------------------------------------------------------------------- | :------: |
| Blender               | For LSCherry                 | <a href="https://www.blender.org/download/">Download</a>                                           | Required |
| Auto Reload Libraries | Auto reload linked libraries | <a href="https://github.com/lvoxx/LSCherry/blob/main/addon/auto_reload_libraries.zip">Download</a> | Required |
| VF PlanarUV           | For Frequent Hair Highlight  | <a href="https://github.com/lvoxx/LSCherry/blob/main/addon/VF_planarUV.py">Download</a>            | Optional |
| Mesh Fairing Master   | Quick Clean Shading Face     | <a href="https://github.com/lvoxx/LSCherry/blob/main/addon/mesh-fairing-master.zip">Download</a>   | Optional |

## 🏁 Getting Started <a name = "getting_started"></a>

1. Download and install at [LSPotato](https://github.com/lvoxx/LSPotato)

[![🌸 Download Addon](https://img.shields.io/badge/Download_Addon-Here-186EDB?style=for-the-badge&logo=github)](https://github.com/lvoxx/LSPotato/releases/latest)

<img width="499" height="254" alt="ảnh" src="docs\assets\addon-preview.png" />

---

3. **Setup**

- Add a Sun Light as the main light source and name it **MLight**.

- Turn on AutoSync mode. For performance reasons, don’t keep it ON in the final Blender file.

> [!TIP]
> You can change any collection and light object name as you want. For best practice I recommend keeping the default MLight and set the collection to be tracked root character collection. </br>
> **Example**
>
> ```
> ├── Character Package -> Set as being tracked collection
> |   ├── Sub Col 1
> |   └── Sub Col 2
> └── MLight -> Set as Sun object
> ```

<img width="auto" height="350" alt="Screenshot 2025-08-31 113739" src="docs\assets\addon-setup.png" />

**Optional**: Make sure Geomery node Core.LSCherryProvider is added to object's modifier and MLight is added to Main Light Dot socket.

<img width="auto" height="268" alt="ảnh" src="https://github.com/user-attachments/assets/b10d5587-65b8-4d66-8900-e23faaae26fe" />

**Optional**: For the best Toon color filter, i recommend you to use Color Management below. Exposure can be around 0.9 to 1.0. If you want to Toon in ArX, use the To ArX output on each main Toon shader.

<img width="auto" height="264" alt="ảnh" src="https://github.com/user-attachments/assets/f94a1afc-962e-402c-b097-c47ab2e1f895" />

---

4. Open Shader Editor and find "Make Toon" node and connect it to Material Output.</br>
   → For others setup and deep knowledge, navigate to [Wiki](https://github.com/lvoxx/LSCherry/wiki)

<img width="auto" height="600" alt="ảnh" src="docs\assets\maketoon-preview.png" />
   
---
5. Yes, its done ✨🎉🎉. If you want to use additional features or pre-built packages, please search for nodes within the materials present in the LSCherry object or those prefixed with "Game Name". Example: HI3, GI, HSR,... find more prefix at [Build-in Toon Support For Games](#build-in)

## 🚀 Quick Start <a name = "quick-start"></a>

Since LSCherry was cross-toon, i has developed many choices for different styles.

- Simple Make Toon: Super quick toon shader, but it has no interaction to the enviroment except the Value.

<img width="auto" height="600" alt="ảnh" src="https://github.com/user-attachments/assets/0659c2c5-5386-4261-8fd1-c6073cd49e81" />

- Stacked Toon: For advanced controll of multi ramp colors, like bush, cloud, tree,...It works alike Simple Make Toon.

<img width="auto" height="450" alt="ảnh" src="https://github.com/user-attachments/assets/d51c2572-531d-49ac-9590-834bac0137f8" />

- ToonRay: For **Cycles Engine** render. Works like Make Toon but it's really hard to custom ramp and no Blended render mode.

<img width="auto" height="450" alt="ảnh" src="https://github.com/user-attachments/assets/8ce7b53a-3f9c-4d67-b0f8-ce71850fd0e5" />

➡ For further documents, [Go To Wiki](https://github.com/lvoxx/LSCherry/wiki)

## 📦 Build-in Toon Support For Games <a name = "build-in"></a>

| Package               |  Prefix  | Starter Pack |
| --------------------- | :------: | :----------: |
| Honkai Impact 3       |   HI3    |      ❌      |
| Genshin Impact        |    GI    |      ❌      |
| Zenless Zone Zero     |   ZZZ    |      ❌      |
| Honkai Starrail       |   HSR    |      ❌      |
| Strinova              | Strinova |      ✔️      |
| Punishing: Gray Raven |   PGR    |      ❌      |
| Girls Frontline 2     |   GF2    |      ❌      |
| Persona Series        |   PSN    |      ❌      |
| Wuthering Waves       |    WW    |      ❌      |
| Aether Gazer          |    AG    |      ❌      |
| Project Snow          |   PJS    |      ❌      |

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
| [<img src="https://github.com/lvoxx.png?size=250" width=115><br><sub>@lvoxx</sub>](https://github.com/lvoxx) <br><br> [![Github-sponsors](https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AAA)](https://www.patreon.com/lvoxxArtist) | [<img src="https://github.com/kitt-cat.png?size=250" width=115><br><sub>@gandalf3</sub>](https://github.com/kitt-cat) <br><br> [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/kitt-cat/auto-reload-linked-libraries) | [<img src="https://github.com/jeinselen.png?size=250" width=115><br><sub>@jeinselen</sub>](https://github.com/jeinselen) <br><br> [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/jeinselen/VF-BlenderPlanarUV) | [<img src="https://github.com/fedackb.png?size=250" width=115><br><sub>@fedackb</sub>](https://github.com/fedackb) <br><br> [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/fedackb/mesh-fairing) |

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

|                                                                                                                                                                   Inspiration by<br>aVersionOfReality                                                                                                                                                                    |
| :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [<img src="https://yt3.googleusercontent.com/3eV9mOZaAJ9Uh16gMaiq8pXwPe9lVlk-K3UR4pkzZ3ggKT7zA-ZZ8GlUqjsvfy6vmIRbURlq=s160-c-k-c0x00ffffff-no-rj" width=115><br>](https://www.youtube.com/@aVersionOfReality)<br> [![Youtube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@aVersionOfReality) |
