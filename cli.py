import argparse
import json
from pathlib import Path

NOTES_FILE = Path.home() / ".personal_notes.json"

def load_notes():
    if NOTES_FILE.exists():
        return json.loads(NOTES_FILE.read_text(encoding="utf-8"))
    return []

def save_notes(notes):
    NOTES_FILE.write_text(json.dumps(notes, indent=2), encoding="utf-8")

def add(text):
    notes = load_notes()
    notes.append(text)
    save_notes(notes)
    print(f"✅ Added note: {text}")

def list_notes():
    notes = load_notes()
    if not notes:
        print("📭 No notes yet.")
    else:
        for i, note in enumerate(notes, start=1):
            print(f"{i}. {note}")

def clear():
    save_notes([])
    print("🗑️ All notes cleared!")

def main():
    parser = argparse.ArgumentParser(description="Personal Notes CLI")
    subparsers = parser.add_subparsers(dest="command")

    # add command
    p_add = subparsers.add_parser("add", help="Add a new note")
    p_add.add_argument("text", nargs="+", help="The note text")

    # list command
    subparsers.add_parser("list", help="List all notes")

    # clear command
    subparsers.add_parser("clear", help="Clear all notes")

    args = parser.parse_args()

    if args.command == "add":
        add(" ".join(args.text))
    elif args.command == "list":
        list_notes()
    elif args.command == "clear":
        clear()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
