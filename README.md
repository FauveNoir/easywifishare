# EasyWifiShare

`easywifishare` est un utilitaire en ligne de commande qui permet de créer des affiches contenant un QRcode et les informations littérales permettant de se connecter à un réseau wifi.

Cet utilitaire utilise LaTeX afin de tirer profit de son rendu.

Ce script est largement inspiré d’une [idée](https://lehollandaisvolant.net/?id=20150201112318) du Hollandais Volant à ce sujet.


## utilisation
De façon générale, `easywifishare` s’utilise de la façon stéréotypée suivante :
<pre>
easywifishare --name <var>nom du réseau</var> --passwd <var>Mot de passe</var> --auth <var>Méthode d’authentification</var> [ --logo | --no-logo ]
</pre>

###Récapitulatif des commandes disponibles

| Commande courte | Commande longue   | Utilité                                                            |
| --------------- | ----------------- | ------------------------------------------------------------------ |
| `-n`            | `--name`          | Nom du réseau                                                      |
| `-p`            | `--passwd`        | Mot de passe du réseau                                             |
| `-a`            | `--auth`          | Méthode d’authentification (`wep`, `wep2`, `wpa`, `wpa2`)          |
| `-i`            | `--ignore-advice` | Ignorer l’avertissement sur la méthode d’authentification          |
|                 | `--no-logo`       | Empêcher l’impression du logotype sous licence de la Wifi Alliance |

# Note légale sur le logotype de la Wifi Alliance
Ne sachant quel licence est exactement attachée au logotype de la Wifi Alliance, je ne me suis permis de l’inclure dans ce petit script que parceque celle-ci utilise son utilisation gratuite pour signaler une zone wifi. Son utilisation n’étant payante que pour les appareils souhaitant signaler qu’ils supportent la technique wifi.

Mon script étant justement lié au signalement des zones wifi il me semble que l’utilisation de ce logotype respecte sa licence de diffusion. Mais corrigez moi si je me trompe :)
