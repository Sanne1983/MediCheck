Das Projekt wurde mit Vite initialisiert:
npm create vite@latest medicheck -- --template react
npm install

Das Projekt (Backend und Frontend) kann folgendermaßen gestartet werden:
Frontend: npm run dev
Backend: python api/api.py

Die Tests können folgendermaßen gestartet werden:
cd api
python -m tests.integration_test_interactions
python -m tests.unittest_dosage_calculation