# LoRaWAN Worker Tracking System Evaluation Project

## Project Overview
This project evaluates a LoRaWAN-based real-time worker tracking system for remote oil palm plantations in Sabah, Malaysia. The goal is to enhance worker safety, optimize workforce management, and improve operational efficiency in challenging plantation environments.

## Key Features
- Real-time worker location tracking
- GPS performance evaluation under dense canopy
- LoRaWAN network coverage assessment
- Interactive web-based tracking and reporting system

## Technical Stack
- Flask (Python web framework)
- SQLAlchemy (Database ORM)
- OpenLayers (Interactive mapping)
- Bootstrap (Frontend styling)

## Backup Information
- Backup Date: 2024-12-15
- Backup Purpose: Project snapshot before deployment
- Excluded Files: SQLite database files

## Deployment Options

### Local Development
1. Clone the repository
2. Create a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
4. Initialize database: `flask db upgrade`
5. Run the application: `flask run`

### Deployment Platforms
- Render
- PythonAnywhere
- Heroku

### GitHub Pages Deployment
- This project is configured for GitHub Pages deployment
- Automatically deploys from the `main` branch
- Static files are published to the `gh-pages` branch

## Environment Variables
- `MAPBOX_ACCESS_TOKEN`: Required for map functionality

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Evaluation Objectives
- Assess LoRaWAN range and coverage
- Evaluate GPS performance under tree canopies
- Test device battery life and functionality
- Analyze cellular signal strength

## Contact
TEQ Armada Sdn Bhd
Sabah, Malaysia
