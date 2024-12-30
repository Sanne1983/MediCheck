import AppLogo from './assets/Logo.png'

function App() {
  // Funktion: Dosierung berechnen
  const calculateDosage = () => {
    const medicationPZN = document.querySelector("#input-section input[placeholder='PZN-Nummer...']").value.trim();
    const weight = document.querySelector("#input-section input[placeholder='Gewicht...']").value.trim();

    // Validierung
    if (!medicationPZN || !weight) {
      alert("Bitte füllen Sie alle Felder aus.");
      return;
    }

    // API-Anfrage für Dosierung
    fetch('http://127.0.0.1:8080/dosage?pzn='+medicationPZN+'&weight='+weight)
      .then(response => {
        if (!response.ok) {
          alert('Bei der Abfrage ist ein Fehler aufgetreten.')
          // Behandlung von HTTP-Fehlern (e.g., 404, 500)
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json(); 
      })
      .then((data) => {
        // Ergebnis anzeigen
        alert('Dosierung für ' + data.name + ': ' + data.dosage_for_weight);
      })
  };

  // Funktion: Wechselwirkungen prüfen
  const checkInteractions = () => {
    const medication1PZN = document.querySelector("#results-section input[placeholder='PZN-Nummer...']").value.trim();
    const medication2PZN = document.querySelector(
      "#results-section input[placeholder='PZN-Nummer...']:nth-of-type(2)"
    ).value.trim();

    // Validierung
    if (!medication1PZN || !medication2PZN) {
      alert("Bitte geben Sie beide PZN-Nummern ein.");
      return;
    }

    // API-Anfrage für Wechselwirkungen
    fetch('http://127.0.0.1:8080/interactions?pzn1='+medication1PZN+'&pzn2='+medication2PZN)
      .then(response => {
        if (!response.ok) {
          alert('Bei der Abfrage ist ein Fehler aufgetreten.')
          // Behandlung von HTTP-Fehlern (e.g., 404, 500)
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json(); 
      })
      .then((data) => {
        // Ergebnis anzeigen
        alert(data.interaction);
      })
  };

  return (
    <>
      <header>
        <div className="header-container">
          <img src={AppLogo} alt="MediCheck Logo" className="header-logo" />
          <h1>MediCheck</h1>
          <p>Interaktiver Medikamentenratgeber</p>
        </div>
      </header>
      <main>
        <section id="input-section">
          <h2>Medikamenten-Dosierung</h2>
          <label for="medication-input">Geben Sie die PZN-Nummer* des Medikaments ein:</label>
          <input type="text" id="medication-input" placeholder="PZN-Nummer..." />
          <label for="medication-input">Geben Sie ihr Gewicht ein (kg):</label>
          <input type="text" id="medication-input" placeholder="Gewicht..." />
          <button onClick={calculateDosage}>Dosierung anzeigen</button>
          <div>*Die achtstellige PZN-Nummer finden Sie auf der Umverpackung ihres Medikaments</div>
        </section>
        <section id="results-section">
          <h2>Arzneimittel-Interaktionen (Wechselwirkungen)</h2>
          <label for="medication-input">Geben Sie die PZN-Nummer* des Medikaments ein:</label>
          <input type="text" id="medication-input" placeholder="PZN-Nummer..." />
          <label for="medication-input">Geben Sie die PZN-Nummer* des Medikaments ein:</label>
          <input type="text" id="medication-input" placeholder="PZN-Nummer..." />
          <button onClick={checkInteractions}>Wechselwirkungen anzeigen</button>
          <div>*Die achtstellige PZN-Nummer finden Sie auf der Umverpackung ihres Medikaments</div>
        </section>
      </main>
    </>
  )
}

export default App
