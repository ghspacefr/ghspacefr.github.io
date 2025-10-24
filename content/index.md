---
title: Home
---

<h4 class="bg-2">ACTUALITÉ</h4>

{% set blog_posts = pages["blog"] | sort(attribute='last_update', reverse=True) %}

{% for item in blog_posts[:3] if not item.subpath.endswith('index.html') %}
- {{ item.last_update }}  [{{ item.title }}](/{{ item.subpath }}){% endfor %}

<h4 class="bg-2">À PROPOS</h4>

<pre>
  .       ____     .      . .            .   
         >>         .        .               .
 .   .  /WWWI; \  .       .    .  ____               .         .     .         
  *    /WWWWII; \=====;    .     /WI; \   *    .        /\_             .
  .   /WWWWWII;..      \_  . ___/WI;:. \     .        _/M; \    .   .         .
     /WWWWWIIIIi;..      \__/WWWIIII:.. \____ .   .  /MMI:  \   * .
 . _/WWWWWIIIi;;;:...:   ;\WWWWWWIIIII;.     \     /MMWII;   \    .  .     .
  /WWWWWIWIiii;;;.:.. :   ;\WWWWWIII;;;::     \___/MMWIIII;   \              .
 /WWWWWIIIIiii;;::.... :   ;|WWWWWWII;;::.:      :;IMWIIIII;:   \___     *
/WWWWWWWWWIIIIIWIIii;;::;..;\WWWWWWIII;;;:::...    ;IMIII;;     ::  \     .
WWWWWWWWWIIIIIIIIIii;;::.;..;\WWWWWWWWIIIII;;..  :;IMIII;:::     :    \   
WWWWWWWWWWWWWIIIIIIii;;::..;..;\WWWWWWWWIIII;::; :::::::::.....::       \
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%XXXXXXX
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%XXXXXXXXXX
</pre>

**GRENOBLE HACKERSPACE** est une association loi 1901, un tier-lieu et une communauté dédiée à la promotion des arts, de l'expérimentation, l'informatique et la cybersécurité. L'association offre un espace de rencontre et de travail pour apprendre, bricoler, collaborer, détourner ensemble.

<h4 class="bg-2">AGENDA</h4>

### Les trucs récurrents

---

**Apéroot**

---

- **Où?**: Au **Tonneau de Diogène, 38100 Grenoble**
- **Quoi?**: Apéro convivial pour rencontrer la communauté autour d’un verre.
- **Quand?**: 1er jeudi du mois, 18h30

---

**Assemblées Générales**

---

- **Où?**: Au local ([voir l'adresse](/contact.html))
- **Quoi?**: Point hebdomadaire pour organiser la vie du lieu (projets, budget, etc.).
- **Quand?**: Quand on peut, les jeudis, 18h30

---

**GRENOBLE HACKERSPACE** participe à d'autres événements, n'hésitez pas à [nous suivre](/contact.html) pour nous retrouver

<h4 class="bg-2">FAQ</h4>

Q : **Faut-il être expert·e pour venir ?** <br>
A : Non ! L’idée est justement d’apprendre ensemble. Seuls prérequis : curiosité et respect du lieu.

Q : **Puis-je venir de manière ponctuelle ?** <br>
A : Bien sûr ! Les Apéroots et certains ateliers sont ouverts à tou·tes.

Q : **Combien ça coûte ?** <br>
A : **Le prix est libre** mais un **abonnement de 16€/mois** est recommandé.

Q : **Qui prend les décisions ?** <br>
A : Chaque décision est validée **collectivement** par ces membres actifs, directement ou pendant les assemblées.

Q : **C’est légal ?** <br>
A : Tout ce qui est fait dans le cadre du lieu respecte la loi. Le reste, *cela ne nous regarde pas* !

<pre>

        |\___/|
        )     (             .              '
       =\     /=
         )===(       *
        /     \
       /       \
       \       /
_/\_/\_/\__  _/_/\_/\_/\_/\_/\_/\_/\_/\_/\_
|  |  |  |( (  |  |  |  |  |  |  |  |  |  |
|  |  |  | )_) |  |  |  |  |  |  |  |  |  |
</pre>
