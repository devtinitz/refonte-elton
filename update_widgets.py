import os
import re

files = ["index.html", "about.html", "products.html", "careers.html", "news.html", "contact.html"]
base_path = "/Users/mac/DOSSIER_MOSES/TINITZ/refonte_elton/"

new_widget = """
<!-- ========================================== -->
<!-- GLOBAL FLOATING WIDGETS (ASSISTANCE & CHAT) -->
<!-- ========================================== -->
<style>
    /* Conteneur Flex global aligné en bas à droite */
    #global-floating-widgets {
        position: fixed;
        bottom: 30px;
        right: 30px;
        z-index: 99999;
        display: flex;
        align-items: flex-end; /* Aligne le bouton assistance et chat par le bas */
        gap: 20px;
        font-family: 'Poppins', sans-serif;
    }

    /* ---- BOUTON ASSISTANCE (Rouge) ---- */
    #btn-assistance-global {
        background-color: #e5003d;
        color: white !important;
        padding: 14px 28px;
        border-radius: 50px;
        display: flex;
        align-items: center;
        gap: 12px;
        font-weight: 700;
        box-shadow: 0 10px 25px rgba(229, 0, 61, 0.4);
        white-space: nowrap;
        transition: all 0.3s ease;
        letter-spacing: 0.5px;
        font-size: 0.9rem;
        cursor: pointer;
        border: none;
        height: 60px; /* Même hauteur que le cercle pour l'alignement */
    }

    #btn-assistance-global:hover {
        transform: translateY(-5px);
        background-color: #c90036;
        box-shadow: 0 15px 35px rgba(229, 0, 61, 0.5);
    }

    /* ---- BOUTON CHAT (Bleu) ---- */
    #btn-chat-global {
        width: 60px;
        height: 60px;
        background-color: #1a73b5;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        box-shadow: 0 10px 25px rgba(26, 115, 181, 0.4);
        transition: transform 0.3s ease, background-color 0.3s ease;
        border: none;
        color: white;
        flex-shrink: 0;
    }

    #btn-chat-global:hover {
        transform: translateY(-5px);
        background-color: #155a8f;
    }

    /* ---- FENÊTRE DE CHAT ---- */
    #chat-window-global {
        position: absolute;
        bottom: 80px; /* S'ouvre juste 20px au-dessus du bouton de 60px */
        right: 0;
        width: 350px;
        background: white;
        border-radius: 15px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.2);
        display: none; /* Masqué par défaut */
        flex-direction: column;
        overflow: hidden;
        animation: slideUpChat 0.3s ease;
    }

    #chat-window-global.active {
        display: flex;
    }

    @keyframes slideUpChat {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* ---- RESPONSIVE MOBILE (<768px) ---- */
    @media (max-width: 768px) {
        #global-floating-widgets {
            bottom: 20px;
            right: 20px;
            flex-direction: column; /* Empiler les widgets verticalement */
            gap: 15px;
            align-items: flex-end;
        }

        #btn-assistance-global {
            padding: 0;           /* Enlève le padding du texte */
            width: 60px;          /* Transforme en cercle parfait */
            height: 60px;
            justify-content: center;
        }

        #btn-assistance-global svg {
            margin: 0; /* Centre l'icône parfaitement */
        }

        #assistance-text-global {
            display: none; /* Masque le texte sur mobile */
        }

        #chat-window-global {
            width: calc(100vw - 40px);
            right: 0;
            bottom: 150px; /* S'ouvre au-dessus des 2 boutons empilés */
        }
    }
</style>

<div id="global-floating-widgets">

    <!-- FENÊTRE DE CHAT INTERACTIVE -->
    <div id="chat-window-global">
        <!-- Header du Chat -->
        <div style="background: #1a73b5; color: white; padding: 20px; display: flex; align-items: center; justify-content: space-between;">
            <h4 style="margin: 0; font-family: 'Ubuntu', sans-serif; display: flex; align-items: center; gap: 10px; font-size: 1.1rem;">
                <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 18v-6a9 9 0 0 1 18 0v6"/><path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3zM3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z"/></svg> 
                Assistant Elton
            </h4>
            <div id="chat-close-global" style="cursor: pointer; display: flex; align-items: center;">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
            </div>
        </div>
        
        <!-- Messages -->
        <div id="chat-messages-global" style="padding: 20px; height: 300px; overflow-y: auto; background: #f9f9f9; display: flex; flex-direction: column; gap: 15px;">
            <div style="background: #e9ecef; padding: 10px 15px; border-radius: 15px 15px 15px 0; max-width: 80%; color: #333; font-size: 0.9rem;">
                Bonjour ! 👋 Comment pouvons-nous vous aider aujourd'hui ?
            </div>
        </div>
        
        <!-- Input du Chat -->
        <div style="padding: 15px; background: white; border-top: 1px solid #eee; display: flex; gap: 10px;">
            <input type="text" id="chat-input-global" placeholder="Écrivez votre message..." style="flex: 1; border: 1px solid #ddd; padding: 10px 15px; border-radius: 20px; font-family: 'Poppins', sans-serif; font-size: 0.9rem; outline: none;">
            <button id="chat-send-global" style="background: #e5003d; border: none; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; cursor: pointer;">
                <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
            </button>
        </div>
    </div>

    <!-- BOUTON ASSISTANCE -->
    <button id="btn-assistance-global">
        <!-- Icône Headset SVG -->
        <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M3 18v-6a9 9 0 0 1 18 0v6"/>
            <path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3zM3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z"/>
        </svg>
        <span id="assistance-text-global">ASSISTANCE 24/7</span>
    </button>

    <!-- BOUTON CHAT -->
    <button id="btn-chat-global">
        <!-- Icône Message SVG -->
        <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
        </svg>
    </button>
</div>

<script>
    // JS 100% Autonome (pas besoin de conflits avec les anciens scripts)
    document.addEventListener("DOMContentLoaded", function() {
        const chatBtn = document.getElementById('btn-chat-global');
        const asstBtn = document.getElementById('btn-assistance-global');
        const chatWin = document.getElementById('chat-window-global');
        const closeBtn = document.getElementById('chat-close-global');
        const inputFld = document.getElementById('chat-input-global');
        const sendBtn = document.getElementById('chat-send-global');
        const msgCont = document.getElementById('chat-messages-global');

        // Basculer l'ouverture du chat (les 2 boutons font la même action)
        const toggleChatUI = () => {
            chatWin.classList.toggle('active');
            if(chatWin.classList.contains('active') && window.innerWidth > 768) {
                inputFld.focus();
            }
        };

        if(chatBtn) chatBtn.addEventListener('click', toggleChatUI);
        if(asstBtn) asstBtn.addEventListener('click', toggleChatUI);
        if(closeBtn) closeBtn.addEventListener('click', toggleChatUI);

        // Envoyer un message et simuler une réponse
        const handleSend = () => {
            const text = inputFld.value.trim();
            if (!text) return;

            // Message utilisateur
            const userBox = document.createElement('div');
            userBox.style.cssText = "background: #1a73b5; color: white; padding: 10px 15px; border-radius: 15px 15px 0 15px; max-width: 80%; align-self: flex-end; font-size: 0.9rem;";
            userBox.textContent = text;
            msgCont.appendChild(userBox);
            inputFld.value = '';
            msgCont.scrollTop = msgCont.scrollHeight;

            // Réponse Bot
            setTimeout(() => {
                const botBox = document.createElement('div');
                botBox.style.cssText = "background: #e9ecef; color: #333; padding: 10px 15px; border-radius: 15px 15px 15px 0; max-width: 80%; font-size: 0.9rem; margin-top: 5px;";
                botBox.textContent = "Merci pour votre message. Un conseiller Elton vous répondra dans un court instant.";
                msgCont.appendChild(botBox);
                msgCont.scrollTop = msgCont.scrollHeight;
            }, 1000);
        };

        if(sendBtn) sendBtn.addEventListener('click', handleSend);
        if(inputFld) {
            inputFld.addEventListener('keypress', (e) => {
                if (e.key === 'Enter') handleSend();
            });
        }
    });
</script>
<!-- ========================================== -->
<!-- FIN GLOBAL FLOATING WIDGETS                -->
<!-- ========================================== -->
"""

for file_name in files:
    filepath = os.path.join(base_path, file_name)
    with open(filepath, 'r') as f:
        content = f.read()

    if "GLOBAL FLOATING WIDGETS" not in content:
        # Supprimer Widgets Flottants
        content = re.sub(r'<!-- Widgets Flottants -->.*?(?=</body>)', '', content, flags=re.DOTALL)
        
        # Supprimer GLOBAL FLOATING ASSISTANCE BUTTON
        content = re.sub(r'<!-- GLOBAL FLOATING ASSISTANCE BUTTON -->.*?(?=</body>)', '', content, flags=re.DOTALL)
        
        # Remplacer vieux chat widget complet
        content = re.sub(r'<!-- Assistance Chat Widget -->.*?</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)
        
        # Supprimer un style restant parfois orphelin
        content = re.sub(r'<style>\s*#sticky-assistance-container.*?</style>', '', content, flags=re.DOTALL)
        
        # Nettoyer d'autres reliquats
        content = re.sub(r'<div id="sticky-assistance-container">.*?</a>\s*</div>', '', content, flags=re.DOTALL)
        
        content = content.replace('</body>', new_widget + '\n</body>')

        with open(filepath, 'w') as f:
            f.write(content)

print("Widgets mis à jour avec succès sur les 6 fichiers !")
