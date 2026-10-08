from playwright.sync_api import sync_playwright

html_content = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    background: #0d1117;
    color: #e6edf3;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    font-size: 14px;
    padding: 18px 34px;
  }
  .breadcrumb {
    text-align: center;
    color: #58a6ff;
    font-size: 12px;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin-bottom: 6px;
  }
  h1 {
    text-align: center;
    color: #58a6ff;
    font-size: 28px;
    font-weight: 700;
    margin-bottom: 6px;
  }
  .subtitle {
    text-align: center;
    color: #8b949e;
    font-size: 13px;
    margin-bottom: 16px;
  }
  .cols {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 14px;
    margin-bottom: 14px;
  }
  .card {
    background: #161b22;
    border: 1px solid #21262d;
    border-radius: 8px;
    overflow: hidden;
  }
  .card-header {
    padding: 12px 18px 8px;
    border-bottom: 1px solid #21262d;
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .card-header .label {
    font-size: 11px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #8b949e;
    display: block;
    margin-bottom: 2px;
  }
  .card-header .title {
    font-size: 17px;
    font-weight: 700;
  }
  .card-header .icon { font-size: 20px; }
  .card-body { padding: 14px 16px; }
  .card.blue { border-top: 3px solid #1f6feb; }
  .card.violet { border-top: 3px solid #8b5cf6; }
  .card.green { border-top: 3px solid #3fb950; }
  .card.blue .card-header .title { color: #58a6ff; }
  .card.violet .card-header .title { color: #c084fc; }
  .card.green .card-header .title { color: #3fb950; }

  .section-title {
    color: #58a6ff;
    font-weight: 600;
    font-size: 13px;
    margin-bottom: 4px;
    margin-top: 10px;
  }
  .section-title:first-child { margin-top: 0; }
  p { color: #8b949e; font-size: 13px; line-height: 1.55; }

  ol { padding-left: 18px; }
  ol li {
    color: #8b949e;
    font-size: 13px;
    line-height: 1.65;
    margin-bottom: 1px;
  }
  code {
    color: #79c0ff;
    background: #0d1117;
    border: 1px solid #30363d;
    border-radius: 4px;
    padding: 1px 6px;
    font-family: 'SFMono-Regular', Consolas, monospace;
    font-size: 12.5px;
  }

  .alert {
    background: #200d0d;
    border: 1px solid #f85149;
    border-radius: 6px;
    padding: 10px 12px;
    margin-top: 12px;
  }
  .alert .alert-title {
    color: #f85149;
    font-weight: 700;
    font-size: 12.5px;
    margin-bottom: 3px;
  }
  .alert p { color: #e6edf3; font-size: 12.5px; }

  .step-check {
    color: #3fb950;
    font-weight: 600;
  }
  .step-indent {
    padding-left: 16px;
    color: #8b949e;
    font-size: 12.5px;
    line-height: 1.5;
    margin-top: 1px;
    margin-bottom: 2px;
  }
  .note {
    color: #8b949e;
    font-size: 12px;
    line-height: 1.55;
    margin-top: 10px;
  }

  .bottom-card {
    background: #161b22;
    border: 1px solid #21262d;
    border-radius: 8px;
    overflow: hidden;
  }
  .bottom-header {
    background: #1c2128;
    padding: 10px 18px;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: 1px solid #21262d;
  }
  .dot { width: 12px; height: 12px; border-radius: 50%; }
  .dot.red { background: #f85149; }
  .dot.yellow { background: #d29922; }
  .dot.green { background: #3fb950; }
  .bottom-label {
    flex: 1;
    text-align: center;
    font-size: 11px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #8b949e;
  }
  .bottom-body { padding: 14px 20px; }
  .bottom-body ol { padding-left: 20px; }
  .bottom-body ol li {
    color: #8b949e;
    font-size: 13px;
    line-height: 1.7;
    font-family: 'SFMono-Regular', Consolas, monospace;
  }
  .bottom-body .warning {
    margin-top: 10px;
    color: #d29922;
    font-size: 12.5px;
    font-family: 'SFMono-Regular', Consolas, monospace;
  }
</style>
</head>
<body>
  <div class="breadcrumb">TD2 · GitHub · Python Data Science — UPJV Amiens</div>
  <h1>Utilisation des Branches GitHub</h1>
  <p class="subtitle">Une branche isole vos modifications sans affecter la version stable. Dans ce cours, chaque TD dispose de sa propre branche avant d'être validé sur main.</p>

  <div class="cols">
    <!-- Colonne 1 -->
    <div class="card blue">
      <div class="card-header">
        <span class="icon">🌿</span>
        <div>
          <span class="label">Concept</span>
          <span class="title">Qu'est-ce qu'une branche ?</span>
        </div>
      </div>
      <div class="card-body">
        <div class="section-title">Travail en isolation</div>
        <p>Chaque branche isole un ensemble de modifications. Les changements d'une branche n'affectent pas les autres tant qu'elles ne sont pas fusionnées.</p>
        <div class="section-title">Éviter les erreurs sur main</div>
        <p>En travaillant sur une branche dédiée, vous ne risquez pas d'écraser accidentellement la version finale et validée de votre travail.</p>
        <div class="section-title">Main = version validée</div>
        <p>La branche main ne contient que des notebooks testés et approuvés. On n'y intègre le travail qu'une fois terminé et relu.</p>
      </div>
    </div>

    <!-- Colonne 2 -->
    <div class="card violet">
      <div class="card-header">
        <span class="icon">⑂</span>
        <div>
          <span class="label">Convention du cours</span>
          <span class="title">Créer votre branche de travail</span>
        </div>
      </div>
      <div class="card-body">
        <p style="margin-bottom:12px;">Nommage obligatoire : <code>dev_tdXX</code> &nbsp;(ex : dev_td03, dev_td04…)</p>
        <ol>
          <li>Onglet <code>Code</code> → icône <code>branches</code></li>
          <li>Cliquer sur <code>New branch</code></li>
          <li>Saisir le nom : <code>dev_td03</code></li>
          <li>Source : <code>main</code> (laisser par défaut)</li>
          <li>Cliquer sur <code>Create branch</code></li>
        </ol>
        <div class="alert">
          <div class="alert-title">⚠ IMPORTANT</div>
          <p>Le nom <strong>dev_tdXX</strong> est obligatoire : GitHub Actions détecte automatiquement le TD à tester à partir du nom de branche.</p>
        </div>
      </div>
    </div>

    <!-- Colonne 3 -->
    <div class="card green">
      <div class="card-header">
        <span class="icon">🔒</span>
        <div>
          <span class="label">À configurer maintenant</span>
          <span class="title">Protéger la branche main</span>
        </div>
      </div>
      <div class="card-body">
        <ol>
          <li>Onglet <code>Settings</code> → section <code>Branches</code></li>
          <li>Cliquer sur <code>Add classic branch protection rule</code></li>
          <li>Branch name pattern : <code>main</code></li>
          <li><span class="step-check">☑</span> <code>Require a pull request before merging</code></li>
          <li>Required approvals : <code>1</code></li>
          <li><span class="step-check">☑</span> <code>Require status checks to pass before merging</code></li>
        </ol>
        <div class="step-indent">Rechercher <code>test</code> → sélectionner <code>Tests TD / test</code></div>
        <ol start="7">
          <li>Cliquer sur <code>Create</code></li>
        </ol>
        <p class="note">Sans cette règle, n'importe qui peut modifier main directement. La règle oblige à passer par une Pull Request approuvée par un pair, avec les tests qui passent.</p>
        <p class="note">Le bouton <strong>Add branch ruleset</strong> juste à côté ouvre l'autre système de règles de GitHub : ce n'est pas celui utilisé ici.</p>
      </div>
    </div>
  </div>

  <!-- Section bas -->
  <div class="bottom-card">
    <div class="bottom-header">
      <span class="dot red"></span>
      <span class="dot yellow"></span>
      <span class="dot green"></span>
      <span class="bottom-label">Navigation entre branches</span>
    </div>
    <div class="bottom-body">
      <ol>
        <li>Onglet Code → cliquer sur le menu déroulant qui affiche le nom de la branche active</li>
        <li>Sélectionner la branche souhaitée dans la liste</li>
        <li>L'explorateur de fichiers se met à jour — chaque branche a son propre contenu indépendant</li>
      </ol>
      <p class="warning">⚠ Un fichier uploadé sur <code>dev_td03</code> n'est pas visible sur <code>main</code> tant qu'il n'a pas été fusionné via une Pull Request validée.</p>
    </div>
  </div>
</body>
</html>"""

OUTPUT = r"assignments/td02_introduction_aux_concepts_de_github/images/07_utilisation_des_branches_pro.png"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1400, "height": 900}, device_scale_factor=2)
    page.set_content(html_content, wait_until="networkidle")
    page.screenshot(path=OUTPUT, full_page=True)
    browser.close()
    print(f"✅ {OUTPUT}")
