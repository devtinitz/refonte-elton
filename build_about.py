import re
import sys

try:
    with open('about.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Split marks
    start_split = html.find('<!-- Content Sections')
    if start_split == -1:
        start_split = html.find('<section id="qui-sommes-nous"')

    end_split = html.find('<!-- Footer -->')

    header = html[:start_split]
    footer = html[end_split:]

    new_content = """
        <!-- Histoire & Introduction -->
        <section id="histoire" class="reveal" style="padding: 100px 5%; background: var(--bg-color);">
            <div class="container" style="max-width: 1200px; margin: 0 auto; display: flex; align-items: stretch; gap: 60px; flex-wrap: wrap;">
                <div style="flex: 1; min-width: 300px; padding: 40px 0;">
                    <span style="color: var(--elton-red); font-weight: 800; letter-spacing: 2px;">NOTRE HISTOIRE</span>
                    <h2 class="section-title" style="margin-top: 10px; font-size: 2.2rem; line-height: 1.3;">ELTON OIL, un partenaire qui vous simplifie la vie</h2>
                    <p style="color: #555; font-size: 1.1rem; line-height: 1.8; margin-bottom: 20px;">
                        En l’an 2000 un groupe d’investisseurs et de professionnels dans la distribution de produits pétroliers faisait le pari de proposer une offre innovante et diversifiée, à la fois conforme aux standards internationaux.
                    </p>
                    <p style="color: #555; font-size: 1.1rem; line-height: 1.8; margin-bottom: 20px;">
                        Tout au long des premières années, nos clients particuliers ou professionnels, nos fournisseurs, nos partenaires, nous ont honorés de leur confiance.
                    </p>
                    <p style="color: #555; font-size: 1.1rem; line-height: 1.8;">
                        Nous poursuivons notre essor en restant à votre écoute pour offrir des produits et services de qualité, en continuant d’innover, en créant de la valeur afin de réinvestir dans nos économies et en offrant des emplois aux jeunes en qui nous avons confiance.
                    </p>
                </div>
                <div style="flex: 1; position: relative; min-width: 300px; display: flex;">
                    <div style="position: absolute; top: 20px; left: -20px; width: 100%; height: calc(100% - 40px); border: 4px solid var(--elton-blue); border-radius: 20px; z-index: 0;"></div>
                    <img src="station.png" alt="Histoire Elton" style="width: 100%; height: auto; object-fit: cover; border-radius: 20px; position: relative; z-index: 1; box-shadow: 0 20px 40px rgba(0,0,0,0.1);">
                </div>
            </div>
        </section>

        <!-- Stats Banner -->
        <section id="stats" style="padding: 60px 5%; background: linear-gradient(135deg, var(--elton-blue) 0%, #0a4f82 100%); position: relative;">
            <div class="grid" style="grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 40px; max-width: 1000px; margin: 0 auto; text-align: center;">
                <div class="reveal hover-lift" style="transition-delay: 0.1s;">
                    <div style="font-size: 4.5rem; font-weight: 800; color: white; line-height: 1; font-family: 'Ubuntu', sans-serif;">12<span style="color: var(--elton-red);">+</span></div>
                    <div style="font-size: 1.1rem; color: rgba(255,255,255,0.8); text-transform: uppercase; margin-top: 10px; font-weight: 600; letter-spacing: 1px;">Ans d'existence</div>
                </div>
                <div class="reveal hover-lift" style="transition-delay: 0.2s;">
                    <div style="font-size: 4.5rem; font-weight: 800; color: white; line-height: 1; font-family: 'Ubuntu', sans-serif;">45<span style="color: var(--elton-red);">+</span></div>
                    <div style="font-size: 1.1rem; color: rgba(255,255,255,0.8); text-transform: uppercase; margin-top: 10px; font-weight: 600; letter-spacing: 1px;">Équipes pros</div>
                </div>
                <div class="reveal hover-lift" style="transition-delay: 0.3s;">
                    <div style="font-size: 4.5rem; font-weight: 800; color: white; line-height: 1; font-family: 'Ubuntu', sans-serif;">215K<span style="color: var(--elton-red);">+</span></div>
                    <div style="font-size: 1.1rem; color: rgba(255,255,255,0.8); text-transform: uppercase; margin-top: 10px; font-weight: 600; letter-spacing: 1px;">Clients fidèles</div>
                </div>
            </div>
        </section>

        <!-- Mission Vision Engagement -->
        <section id="raison-etre" style="padding: 100px 5%; background: #f9fbfd;">
            <div style="text-align: center; margin-bottom: 70px;" class="reveal">
                <span style="color: var(--elton-red); font-weight: 800; letter-spacing: 2px;">POURQUOI NOUS EXISTONS ?</span>
                <h2 class="section-title" style="margin-top: 10px; display: block;">Notre ADN</h2>
                <p style="color: #666; max-width: 800px; margin: 0 auto; font-size: 1.1rem;">Notre souci permanent est de mettre tout notre potentiel humain au service exclusif de la satisfaction des besoins de nos clients.</p>
            </div>
            
            <div class="grid" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 40px; max-width: 1200px; margin: 0 auto;">
                <!-- Mission -->
                <div class="card reveal hover-lift" style="background: white; padding: 40px; border-radius: 20px; text-align: center; border-top: 5px solid var(--elton-blue); box-shadow: 0 15px 35px rgba(0,0,0,0.05);">
                    <div style="width: 80px; height: 80px; background: rgba(26,115,181,0.1); border-radius: 50%; color: var(--elton-blue); display: flex; align-items: center; justify-content: center; margin: 0 auto 25px auto;">
                        <i data-lucide="target" style="width: 40px; height: 40px;"></i>
                    </div>
                    <h3 style="color: var(--elton-blue); margin-bottom: 15px; font-size: 1.4rem;">Notre Mission</h3>
                    <p style="color: #666; line-height: 1.7; font-size: 1rem;">Offrir à chaque client une énergie fiable et accessible, tout en garantissant un service de qualité, une sécurité optimale et une satisfaction durable à travers des solutions adaptées à tous les besoins de mobilité.</p>
                </div>
                <!-- Vision -->
                <div class="card reveal hover-lift test-transform" style="background: white; padding: 40px; border-radius: 20px; text-align: center; border-top: 5px solid var(--elton-red); box-shadow: 0 20px 40px rgba(0,0,0,0.08);">
                    <div style="width: 80px; height: 80px; background: rgba(229,0,61,0.1); border-radius: 50%; color: var(--elton-red); display: flex; align-items: center; justify-content: center; margin: 0 auto 25px auto;">
                        <i data-lucide="eye" style="width: 40px; height: 40px;"></i>
                    </div>
                    <h3 style="color: var(--elton-red); margin-bottom: 15px; font-size: 1.4rem;">Notre Vision</h3>
                    <p style="color: #666; line-height: 1.7; font-size: 1rem;">Devenir une référence nationale dans la distribution d’énergie et de services, en innovant continuellement pour offrir une expérience moderne, responsable et centrée sur la confiance de nos clients.</p>
                </div>
                <!-- Engagement -->
                <div class="card reveal hover-lift" style="background: white; padding: 40px; border-radius: 20px; text-align: center; border-top: 5px solid var(--elton-blue); box-shadow: 0 15px 35px rgba(0,0,0,0.05);">
                    <div style="width: 80px; height: 80px; background: rgba(26,115,181,0.1); border-radius: 50%; color: var(--elton-blue); display: flex; align-items: center; justify-content: center; margin: 0 auto 25px auto;">
                        <i data-lucide="shield-check" style="width: 40px; height: 40px;"></i>
                    </div>
                    <h3 style="color: var(--elton-blue); margin-bottom: 15px; font-size: 1.4rem;">Notre Engagement</h3>
                    <p style="color: #666; line-height: 1.7; font-size: 1rem;">Nous nous engageons à respecter les normes de qualité et de sécurité, à servir nos clients avec professionnalisme et à contribuer durablement au développement des communautés que nous accompagnons.</p>
                </div>
            </div>
            
            <div style="text-align: center; max-width: 900px; margin: 60px auto 0 auto; color: var(--elton-blue); font-size: 1.1rem; line-height: 1.8; font-style: italic; font-weight: 500;" class="reveal">
                " Ainsi, nous entendons densifier le maillage de notre couverture régionale par l’ouverture de nouvelles stations, diversifier plus encore nos produits et services, et entamer le processus de certification. "
            </div>
        </section>

        <!-- Nos activités -->
        <section id="activites" style="padding: 100px 5%; background: white;">
            <div style="text-align: center; margin-bottom: 70px;" class="reveal">
                <h2 class="section-title">Nos Activités</h2>
                <p style="color: #666; max-width: 800px; margin: 0 auto; font-size: 1.1rem;">ELTON est présent au Sénégal au travers de ses activités de distribution de produits pétroliers (Refining & Marketing) et de services.</p>
            </div>
            
            <div class="grid" style="grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 50px; max-width: 1200px; margin: 0 auto;">
                <!-- Distribution Area -->
                <div style="background: url('hero_fallback.jpg') center/cover; padding: 40px; border-radius: 20px; color: white; position: relative; overflow: hidden; display: flex; flex-direction: column; justify-content: flex-end; min-height: 450px; box-shadow: 0 20px 40px rgba(0,0,0,0.2);" class="hover-lift reveal">
                    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(0deg, rgba(0,16,33,0.95) 0%, rgba(26,115,181,0.5) 100%); z-index: 0;"></div>
                    <div style="position: relative; z-index: 1;">
                        <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                            <i data-lucide="truck" style="color: var(--elton-red); width: 45px; height: 45px;"></i>
                            <h3 style="font-size: 2.2rem; margin: 0; font-family: 'Ubuntu', sans-serif;">Distribution</h3>
                        </div>
                        <p style="font-size: 1.05rem; line-height: 1.7; opacity: 0.9; margin-bottom: 25px;">
                            ELTON opère dans le domaine de la commercialisation des produits issus du raffinage du pétrole. Les carburants issus des raffineries sont proposés aux clients dans le réseau des stations-service ELTON.
                        </p>
                        <div style="display: flex; align-items: flex-start; gap: 10px; margin-bottom: 12px; font-size: 0.95rem;">
                            <i data-lucide="check-circle" style="color: var(--elton-red); width: 22px; flex-shrink: 0; margin-top: 2px;"></i>
                            <span style="font-family: 'Poppins', sans-serif;">Représentant exclusif de la marque de Lubrifiants Castrol.</span>
                        </div>
                        <div style="display: flex; align-items: flex-start; gap: 10px; font-size: 0.95rem;">
                            <i data-lucide="check-circle" style="color: var(--elton-red); width: 22px; flex-shrink: 0; margin-top: 2px;"></i>
                            <span style="font-family: 'Poppins', sans-serif;">Exporte des produits pétroliers dans la sous-région (Mali, Gambie, Guinée, Guinée Bissau).</span>
                        </div>
                    </div>
                </div>
                
                <!-- Produits Spéciaux Area -->
                <div style="background: url('car1.png') center/cover; padding: 40px; border-radius: 20px; color: white; position: relative; overflow: hidden; display: flex; flex-direction: column; justify-content: flex-end; min-height: 450px; box-shadow: 0 20px 40px rgba(0,0,0,0.2);" class="hover-lift reveal">
                    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(0deg, rgba(229,0,61,0.95) 0%, rgba(229,0,61,0.5) 100%); z-index: 0;"></div>
                    <div style="position: relative; z-index: 1;">
                        <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                            <i data-lucide="package" style="color: white; width: 45px; height: 45px;"></i>
                            <h3 style="font-size: 2.2rem; margin: 0; font-family: 'Ubuntu', sans-serif;">Produits Spéciaux</h3>
                        </div>
                        <p style="font-size: 1.05rem; line-height: 1.7; opacity: 0.9; margin-bottom: 25px;">
                            Les produits spéciaux comme la pompe pêche, les graisses industrielles et lubrifiants de matériel agricole ainsi que les produits dédiés aux professionnels sont commercialisés.
                        </p>
                        <div style="display: flex; align-items: flex-start; gap: 10px; margin-bottom: 12px; font-size: 0.95rem;">
                            <i data-lucide="check-circle" style="color: white; width: 22px; flex-shrink: 0; margin-top: 2px;"></i>
                            <span style="font-family: 'Poppins', sans-serif;">Offre de services diversifiés dans notre réseau de Boutique.</span>
                        </div>
                        <div style="display: flex; align-items: flex-start; gap: 10px; font-size: 0.95rem;">
                            <i data-lucide="check-circle" style="color: white; width: 22px; flex-shrink: 0; margin-top: 2px;"></i>
                            <span style="font-family: 'Poppins', sans-serif;">Fournisseurs de produits et services liés aux carburants et lubrifiants aux PME et PMI.</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Leadership Messages -->
        <section id="leadership" class="reveal" style="padding: 100px 5%; background: var(--bg-color);">
            <h2 class="section-title" style="text-align:center; display:block; margin-bottom: 60px;">Notre Leadership</h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 40px; max-width: 1200px; margin: 0 auto;" id="leadership-grid">
                <!-- President Card -->
                <div id="mot-president" class="card hover-lift" style="padding: 0; overflow: hidden; display: flex; flex-direction: row; text-align: left; min-height: 300px; background: white; border: none; box-shadow: 0 15px 35px rgba(0,0,0,0.05);">
                    <div style="width: 40%; background: linear-gradient(135deg, var(--elton-blue) 0%, #0a4f82 100%); display: flex; align-items: center; justify-content: center; position: relative; color: white; padding: 30px; text-align: center;">
                            <i data-lucide="user-check" style="width: 60px; height: 60px; opacity: 0.2; position: absolute; top: 30px;"></i>
                            <div style="z-index: 1; margin-top: 40px;">
                                <div style="font-weight: 800; font-size: 1.1rem; margin-bottom: 5px;">Pr. Papa Madiaw NDIAYE</div>
                                <div style="font-size: 0.8rem; opacity: 0.8;">Président du C.A.</div>
                            </div>
                    </div>
                    <div style="width: 60%; padding: 40px; position: relative; display: flex; flex-direction: column; justify-content: center;">
                        <i data-lucide="quote" style="position: absolute; top: 20px; right: 20px; width: 40px; height: 40px; color: rgba(229,0,61,0.05);"></i>
                        <h4 style="color: var(--elton-blue); margin-bottom: 15px; font-family: 'Ubuntu', sans-serif; font-size: 1.2rem;">Mot du Président</h4>
                        <p style="font-style: italic; color: #555; line-height: 1.6; font-size: 0.95rem; margin: 0;">"Notre ambition est de faire d'Elton une référence absolue de l'énergie en Afrique, en alliant innovation constante et respect de nos engagements historiques envers nos partenaires."</p>
                    </div>
                </div>

                <!-- DG Card -->
                <div id="mot-dg" class="card hover-lift" style="padding: 0; overflow: hidden; display: flex; flex-direction: row; text-align: left; min-height: 300px; background: white; border: none; box-shadow: 0 15px 35px rgba(0,0,0,0.05);">
                    <div style="width: 40%; background: linear-gradient(135deg, var(--elton-red) 0%, #a60029 100%); display: flex; align-items: center; justify-content: center; position: relative; color: white; padding: 30px; text-align: center;">
                            <i data-lucide="user-check" style="width: 60px; height: 60px; opacity: 0.2; position: absolute; top: 30px;"></i>
                            <div style="z-index: 1; margin-top: 40px;">
                                <div style="font-weight: 800; font-size: 1.1rem; margin-bottom: 5px;">M. Babacar TALL</div>
                                <div style="font-size: 0.8rem; opacity: 0.8;">Directeur Général</div>
                            </div>
                    </div>
                    <div style="width: 60%; padding: 40px; position: relative; display: flex; flex-direction: column; justify-content: center;">
                        <i data-lucide="quote" style="position: absolute; top: 20px; right: 20px; width: 40px; height: 40px; color: rgba(26,115,181,0.05);"></i>
                        <h4 style="color: var(--elton-red); margin-bottom: 15px; font-family: 'Ubuntu', sans-serif; font-size: 1.2rem;">Mot du D.G.</h4>
                        <p style="font-style: italic; color: #555; line-height: 1.6; font-size: 0.95rem; margin: 0;">"Chez Elton, nous plaçons l'humain au cœur de nos stations. Chaque visiteur doit vivre une expérience de service unique, fluide et de la plus haute qualité."</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- FAQ Accordion -->
        <section id="faq" style="padding: 100px 5%; background: white;" class="reveal">
            <div style="text-align: center; margin-bottom: 60px;">
                <h2 class="section-title">Questions fréquemment posées</h2>
                <p style="color: #666; font-size: 1.1rem;">Trouvez les réponses à vos questions les plus courantes sur Elton Group.</p>
            </div>
            <div style="max-width: 900px; margin: 0 auto; display: flex; flex-direction: column; gap: 20px;">
                
                <details style="background: var(--bg-color); border-radius: 15px; padding: 25px; box-shadow: 0 5px 15px rgba(0,0,0,0.03); cursor: pointer; border-left: 5px solid var(--elton-blue); transition: 0.3s;" onmouseover="this.style.transform='translateX(5px)'" onmouseout="this.style.transform='translateX(0)'">
                    <summary style="font-weight: 700; color: var(--elton-dark); font-size: 1.15rem; list-style: none; display: flex; justify-content: space-between; align-items: center; font-family: 'Poppins', sans-serif;">Présence d'ELTON en Côte d'Ivoire ? <i data-lucide="chevron-down" style="color: var(--elton-red);"></i></summary>
                    <div style="margin-top: 20px; color: #555; line-height: 1.7; border-top: 1px solid rgba(0,0,0,0.05); padding-top: 20px; font-size: 1rem; font-family: 'Poppins', sans-serif;">Oui — Elton Oil Company opère aussi en Gambie et Sénégal et possède des filiales dans plusieurs pays d’Afrique de l’Ouest, avec des services complémentaires dans certaines stations.</div>
                </details>
                
                <details style="background: var(--bg-color); border-radius: 15px; padding: 25px; box-shadow: 0 5px 15px rgba(0,0,0,0.03); cursor: pointer; border-left: 5px solid var(--elton-blue); transition: 0.3s;" onmouseover="this.style.transform='translateX(5px)'" onmouseout="this.style.transform='translateX(0)'">
                    <summary style="font-weight: 700; color: var(--elton-dark); font-size: 1.15rem; list-style: none; display: flex; justify-content: space-between; align-items: center; font-family: 'Poppins', sans-serif;">Est-ce qu’ELTON propose d’autres services qu’une simple pompe à carburant ? <i data-lucide="chevron-down" style="color: var(--elton-red);"></i></summary>
                    <div style="margin-top: 20px; color: #555; line-height: 1.7; border-top: 1px solid rgba(0,0,0,0.05); padding-top: 20px; font-size: 1rem; font-family: 'Poppins', sans-serif;">Absolument, nos stations sont de véritables "Oasis" proposant boutiques, espaces café, lavage auto de pointe équipés des dernières technologies à vapeur, et services financiers.</div>
                </details>

                <details style="background: var(--bg-color); border-radius: 15px; padding: 25px; box-shadow: 0 5px 15px rgba(0,0,0,0.03); cursor: pointer; border-left: 5px solid var(--elton-blue); transition: 0.3s;" onmouseover="this.style.transform='translateX(5px)'" onmouseout="this.style.transform='translateX(0)'">
                    <summary style="font-weight: 700; color: var(--elton-dark); font-size: 1.15rem; list-style: none; display: flex; justify-content: space-between; align-items: center; font-family: 'Poppins', sans-serif;">Où se trouvent les stations services d'ELTON ? <i data-lucide="chevron-down" style="color: var(--elton-red);"></i></summary>
                    <div style="margin-top: 20px; color: #555; line-height: 1.7; border-top: 1px solid rgba(0,0,0,0.05); padding-top: 20px; font-size: 1rem; font-family: 'Poppins', sans-serif;">Notre maillage territorial couvre massivement les principales agglomérations et axes routiers majeurs. Vous pouvez facilement <a href="contact.html#station-map" style="color: var(--elton-red); font-weight: 600;">trouver la carte complète ici</a>.</div>
                </details>

                <details style="background: var(--bg-color); border-radius: 15px; padding: 25px; box-shadow: 0 5px 15px rgba(0,0,0,0.03); cursor: pointer; border-left: 5px solid var(--elton-blue); transition: 0.3s;" onmouseover="this.style.transform='translateX(5px)'" onmouseout="this.style.transform='translateX(0)'">
                    <summary style="font-weight: 700; color: var(--elton-dark); font-size: 1.15rem; list-style: none; display: flex; justify-content: space-between; align-items: center; font-family: 'Poppins', sans-serif;">Quels types de carburants sont disponibles ? <i data-lucide="chevron-down" style="color: var(--elton-red);"></i></summary>
                    <div style="margin-top: 20px; color: #555; line-height: 1.7; border-top: 1px solid rgba(0,0,0,0.05); padding-top: 20px; font-size: 1rem; font-family: 'Poppins', sans-serif;">Nous proposons une gamme complète de carburants (Super Sans Plomb, Gasoil) raffinés aux meilleurs standards internationaux, ainsi que toute la gamme haute performance Castrol.</div>
                </details>

                <details style="background: var(--bg-color); border-radius: 15px; padding: 25px; box-shadow: 0 5px 15px rgba(0,0,0,0.03); cursor: pointer; border-left: 5px solid var(--elton-blue); transition: 0.3s;" onmouseover="this.style.transform='translateX(5px)'" onmouseout="this.style.transform='translateX(0)'">
                    <summary style="font-weight: 700; color: var(--elton-dark); font-size: 1.15rem; list-style: none; display: flex; justify-content: space-between; align-items: center; font-family: 'Poppins', sans-serif;">Peut-on payer par carte ou y-a-t-il des services supplémentaires ? <i data-lucide="chevron-down" style="color: var(--elton-red);"></i></summary>
                    <div style="margin-top: 20px; color: #555; line-height: 1.7; border-top: 1px solid rgba(0,0,0,0.05); padding-top: 20px; font-size: 1rem; font-family: 'Poppins', sans-serif;">Oui, Elton propose sa propre <strong>Carte Elton Oasis</strong> pour les particuliers ou les professionnels, permettant un suivi digital en temps réel. Nous acceptons également tous types de paiements classiques.</div>
                </details>
            </div>
            
            <style>
                details > summary::-webkit-details-marker { display: none; }
                details[open] summary i { transform: rotate(180deg); }
                details summary i { transition: transform 0.4s; }
                @media(min-width: 968px) {
                    .test-transform { transform: translateY(-20px); }
                }
            </style>
        </section>

        <!-- Nos Partenaires Section -->
        <section id="partenaires" style="padding: 100px 5%; background: var(--bg-color); text-align: center;" class="reveal">
            <h2 class="section-title">Nos Partenaires</h2>
            <p style="color: #666; font-size: 1.1rem; margin-bottom: 50px;">Ils nous font confiance au quotidien</p>
            <div style="display: flex; justify-content: center; gap: 40px; flex-wrap: wrap; opacity: 0.6; filter: grayscale(100%); max-width: 1200px; margin: 0 auto;">
                <div style="width: 160px; height: 90px; background: white; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-weight: 800; color: #aaa; box-shadow: 0 5px 15px rgba(0,0,0,0.05); transition: 0.3s;" onmouseover="this.style.filter='grayscale(0%)'; this.style.opacity='1'; this.style.transform='translateY(-5px)'" onmouseout="this.style.filter='grayscale(100%)'; this.style.opacity='0.6'; this.style.transform='translateY(0)'"><i data-lucide="building" style="margin-right: 10px;"></i> PME/PMI</div>
                <div style="width: 160px; height: 90px; background: white; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-weight: 800; color: #aaa; box-shadow: 0 5px 15px rgba(0,0,0,0.05); transition: 0.3s;" onmouseover="this.style.filter='grayscale(0%)'; this.style.opacity='1'; this.style.transform='translateY(-5px)'" onmouseout="this.style.filter='grayscale(100%)'; this.style.opacity='0.6'; this.style.transform='translateY(0)'"><i data-lucide="car" style="margin-right: 10px;"></i> TOYOTA</div>
                <div style="width: 160px; height: 90px; background: white; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-weight: 800; color: #aaa; box-shadow: 0 5px 15px rgba(0,0,0,0.05); transition: 0.3s;" onmouseover="this.style.filter='grayscale(0%)'; this.style.opacity='1'; this.style.transform='translateY(-5px)'" onmouseout="this.style.filter='grayscale(100%)'; this.style.opacity='0.6'; this.style.transform='translateY(0)'"><i data-lucide="activity" style="margin-right: 10px;"></i> CASTROL</div>
                <div style="width: 160px; height: 90px; background: white; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-weight: 800; color: #aaa; box-shadow: 0 5px 15px rgba(0,0,0,0.05); transition: 0.3s;" onmouseover="this.style.filter='grayscale(0%)'; this.style.opacity='1'; this.style.transform='translateY(-5px)'" onmouseout="this.style.filter='grayscale(100%)'; this.style.opacity='0.6'; this.style.transform='translateY(0)'"><i data-lucide="factory" style="margin-right: 10px;"></i> SAR</div>
                <div style="width: 160px; height: 90px; background: white; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-weight: 800; color: #aaa; box-shadow: 0 5px 15px rgba(0,0,0,0.05); transition: 0.3s;" onmouseover="this.style.filter='grayscale(0%)'; this.style.opacity='1'; this.style.transform='translateY(-5px)'" onmouseout="this.style.filter='grayscale(100%)'; this.style.opacity='0.6'; this.style.transform='translateY(0)'"><i data-lucide="briefcase" style="margin-right: 10px;"></i> B2B</div>
            </div>
        </section>
"""

    # Stitch together
    final_html = header + new_content + footer

    with open('about.html', 'w', encoding='utf-8') as f:
        f.write(final_html)
    print("Successfully built about.html")
except Exception as e:
    print(f"Error: {e}")
