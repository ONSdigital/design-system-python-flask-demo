import os,json

scenarios = []
root_directory = 'templates/components'
directories = [name for name in os.listdir(root_directory)]
example_files = [f'components/{directory}/{file}' for directory in directories for file in os.listdir(os.path.join(root_directory, directory)) if file.startswith('example')]

for url in example_files:
    scenarios.append({
        "label": url.replace('.njk',''),
        "url": f"http://127.0.0.1:5000/{url}",
        "referenceUrl": "",
        "readyEvent": "",
        "readySelector": "",
        "delay": 1000,
        "hideSelectors": ["p.ons-js-timeout-timer span"] if url == 'components/timeout-panel/example-panel-with-timeout-warning.njk' else [],
        "removeSelectors": [],
        "hoverSelector": "",
        "clickSelector": "",
        "postInteractionWait": 0,
        "selectors": [],
        "selectorExpansion": True,
        "expect": 0,
        "misMatchThreshold": 0.05,
        "requireSameDimensions": True
    })

config = {
    "id": "ds-vr-test",
    "viewports": [
        {
        "label": "desktop",
        "width": 1920,
        "height": 1080
        },
        {
        "label": "phone",
        "width": 375,
        "height": 667
        },
        {
        "label": "tablet",
        "width": 768,
        "height": 1024
        }
    ],
    "scenarios": scenarios,
    "paths": {
        "bitmaps_reference": "backstop_data/bitmaps_reference",
        "bitmaps_test": "backstop_data/bitmaps_test",
        "engine_scripts": "backstop_data/engine_scripts",
        "html_report": "backstop_data/html_report",
        "ci_report": "backstop_data/ci_report",
},
"engine": "puppeteer",
"engineOptions": {
    "args": [
    "--disable-gpu",
    "--no-sandbox",
    "--disable-setuid-sandbox",
    "--shm-size=512mb",
    "--disable-dev-shm-usage",
    "--cap-add=SYS_ADMIN",
    ],
},
}

with open('backstop.json', 'w') as f:
    json.dump(config, f, indent=4)


