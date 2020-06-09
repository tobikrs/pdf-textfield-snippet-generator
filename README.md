# PDF Placeholder Editor

Mit hilfe des Programms [Xournal++](https://github.com/xournalpp/xournalpp) ist es möglich ein Platzhaltern über einen graphische Oberfläche auf einem PDF zu platzieren und PHP-Code daraus zu generieren.


## Requirements

 - Python 3.7+
 - [Xournal++](https://github.com/xournalpp/xournalpp)


## Quickstart

1. Öffne ein PDF mit Xournal++

2. Füge Texte an den gewünschten Stellen ein.

3. Speichere die Xournal-Datei unter `editor.xopp` im Projekt-Verzeichnis.

4. Änderen je nach belieben das Template `template.txt` bestehend aus den Platzhaltern `|x|` und `|y|` für die Koordinaten der jeweiligen Textfelder und `|text|` für den geschrieben Text.

5. Starte den Generator mit `python generator.py`.

6. Schaue dir das Ergebnis im `output.txt` an. Fall du zu Frieden bist, füge es in deinen Sourcecode ein.

7. Justiere ggf. ein paar der Koordinaten-Werte nach.


## Datein und ihre Bedeutung

### Xournal++ Datei `editor.xopp`

Diese Datei speichert den Zustand des Xournal++-Editors.
Das setzten der Text-Felder ist in der graphischen Oberfläche deutlich einfacher als wert über den Sourcecode auszuprobieren.

### Template `template.txt`

Mit dieser Datei bestimmst du in welchen Format Text und Koordinaten der Text-Felder für deinen Sourcecode generiert werden. Um die entsprechenden Werte einzusetzten müssen an den gewüschten Stellen die Platzhalter `|text|`, `|x|` und `|y|` eingefügt werden.

### Generator `generator.py`

> This is were the magic happens...

Dieses Script parst den Objekte-Baum der Xournal++-Datei, liest den Text und die Koordinaten der Text-Felder aus und speichert diese dem Template `template.txt` entsprechend in `output.txt
