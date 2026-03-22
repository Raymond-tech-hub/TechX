# setup_techx_structure.py
# Run this script from the parent directory where you want TechX/ to be created
# Example: python setup_techx_structure.py

import os

# Root folder
ROOT = "TechX"

# All folders we want (relative to ROOT)
FOLDERS = [
    "public",
    "public/images",
    "public/fonts",
    
    "src",
    "src/app",
    "src/app/products",
    "src/app/products/lumina",
    "src/app/products/nova",
    "src/app/services",
    "src/app/about",
    "src/app/blog",
    "src/app/blog/[slug]",
    "src/app/contact",
    "src/app/api",
    "src/app/api/contact",
    
    "src/components",
    "src/components/ui",
    "src/components/layout",
    "src/components/product",
    "src/components/sections",
    
    "src/lib",
    "src/hooks",
    "src/data",
    "src/types",
]

# Placeholder files (only small important ones to start)
FILES = {
    # Root level
    f"{ROOT}/README.md": "# TechX\n\nFrom Curiosity to Legacy: Pioneering AI Excellence\n",
    f"{ROOT}/.gitignore": "node_modules/\n.next/\nout/\n.DS_Store\n.env.local\n",
    
    # public/
    f"{ROOT}/public/robots.txt": "User-agent: *\nDisallow: /",
    
    # src/app/
    f"{ROOT}/src/app/layout.tsx": "// Root layout\n\nexport default function RootLayout({ children }) {\n  return (\n    <html lang=\"en\">\n      <body>{children}</body>\n    </html>\n  );\n}\n",
    f"{ROOT}/src/app/page.tsx": "// Home page\n\nexport default function Home() {\n  return <main>Home - TechX</main>;\n}\n",
    f"{ROOT}/src/app/globals.css": "/* Global styles */\n@tailwind base;\n@tailwind components;\n@tailwind utilities;\n",
    
    # A few example component & data files
    f"{ROOT}/src/components/layout/Header.tsx": "// Header component\n\nexport default function Header() {\n  return <header>TechX Navigation</header>;\n}\n",
    f"{ROOT}/src/data/team.ts": "// Team data\nexport const team = [];\n",
    f"{ROOT}/src/lib/constants.ts": "// Constants\nexport const TAGLINE = \"From Curiosity to Legacy: Pioneering AI Excellence\";\n",
}

def create_structure():
    print(f"Creating TechX project structure in: ./{ROOT}\n")
    
    # Create all folders
    created_folders = 0
    for folder in FOLDERS:
        path = os.path.join(ROOT, folder)
        if not os.path.exists(path):
            os.makedirs(path)
            created_folders += 1
            print(f"Created folder: {path}")
        # else:
        #     print(f"Already exists: {path}")
    
    print(f"\n→ Created/checked {created_folders} new folders\n")
    
    # Create placeholder files
    created_files = 0
    for filepath, content in FILES.items():
        if not os.path.exists(filepath):
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            created_files += 1
            print(f"Created file: {filepath}")
        # else:
        #     print(f"Already exists: {filepath}")
    
    print(f"\n→ Created/checked {created_files} new files")
    print("\nSetup complete! You can now:")
    print("  cd TechX")
    print("  npm init -y          # or yarn init -y")
    print("  npx create-next-app@latest . --use-npm --typescript --tailwind --eslint --app --src-dir --import-alias \"@/*\"")
    print("    (answer yes when it asks to proceed)\n")

if __name__ == "__main__":
    if os.path.exists(ROOT) and os.listdir(ROOT):
        print(f"Warning: Directory '{ROOT}' already exists and is not empty.")
        answer = input("Continue anyway? (y/N): ").strip().lower()
        if answer not in ('y', 'yes'):
            print("Aborted.")
            exit(0)
    
    create_structure()