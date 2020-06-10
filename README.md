# PDF Placeholder Editor

Mit hilfe des Editors [Xournal++](https://github.com/xournalpp/xournalpp) ist es möglich Textfelder über eine graphische Oberfläche auf einem PDF zu platzieren und Snippets daraus zu generieren.

Ich benutzte dieses Projekt ursprünglich um mir das Einfügen von Texten (Platzhalter) in ein PDF in PHP mit der [Library FPDF](http://fpdf.de/start.html) zu erleichtern.  
Durch das Ändern der `template.txt` und der ersten Zeile von `output` in `generator.py:30` ist aber die Generierung von Snippets in anderen Sprachen auch möglich.


## Requirements

 - Python 3.7+
 - [Xournal++](https://github.com/xournalpp/xournalpp)


## Quickstart

1. Öffne ein PDF mit Xournal++

2. Füge Texte an den gewünschten Stellen ein.

3. Speichere die Xournal-Datei unter `editor.xopp` im Projekt-Verzeichnis.

4. Ändere je nach belieben das Template `template.txt` bestehend aus den Platzhaltern `|x|` und `|y|` für die Koordinaten der jeweiligen Textfelder und Platzhalter `|text|` für den Inhalt des Textfeldes.

5. Generiere den PHP-Snippet durch Ausführen des Python-Scripts mit `python generator.py`.

6. Schaue dir das Ergebnis im `snippet.php` an. Falls du zu Frieden bist, füge es in deinen Sourcecode ein.

7. Ggf. ist es notwendig die Koordinaten im Sourcecode nachzujustieren.


## Datein und ihre Bedeutung

### Xournal++ Datei `editor.xopp`

Diese Datei speichert den Zustand des Xournal++-Editors.
Das setzten der Text-Felder ist in der graphischen Oberfläche deutlich einfacher als wert über den Sourcecode auszuprobieren.

### Objekte-Baum `object_tree.xml`

Diese Datei bildet die Struktur der Xournal++-Datei als Baum im XML-Format ab.

Beispiel:
```
<?xml version="1.0" standalone="no"?>
<xournal creator="Xournal++ 1.0.16" fileversion="4">
    <title>...</title>

    <page width="595.27600000" height="841.89000000">
        <background type="pdf" domain="absolute" filename="/path/to/your.pdf" pageno="1ll"/>
        <layer>
            <text ... x="78.94074957" y="176.71081941" ...>1. In a new window of Xournal++ click on 'File' &gt; 'Open'.</text>
            <text ... x="78.93844351" y="214.95407886" ...>2. Choose your PDF.</text>
            <text ... x="75.48190998" y="251.82592425" ...>3. Start adding text fields at the desired position.</text>
            <text ... x="57.03565556" y="144.80251444" ...>Follow these  guide to add text to your PDF.  </text>
            <text ... x="55.05548263" y="58.41392332" ...>Dummy Editor-File</text>
        <layer/>
    </page>

</xournal>

```

### Template `template.txt`

Mit dieser Datei bestimmst du in welchen Format Text und Koordinaten der Text-Felder für deinen Sourcecode generiert werden. Um die entsprechenden Werte einzusetzten müssen an den gewüschten Stellen die Platzhalter `|text|`, `|x|` und `|y|` eingefügt werden.

Beispiel:
```

    $pdf->SetXY(|x|, |y|+$y);
    $pdf->write(0, "|text|");


```

### Generator `generator.py`

> This is were the magic happens...

Dieses Script parst den Objekte-Baum der Xournal++-Datei, liest den Text und die Koordinaten der Text-Felder aus und speichert diese dem Template `template.txt` entsprechend in `snippet.php`.


### Snippet `snippet.php`

Hier findest du das generierte Snippet.

Mal angenommen aus den oben gegeben Beispielen würde ein Snippet generiert werden, dann sehe es so aus:
```
<?php
# Here is your generated snippet:

    $pdf->SetXY(26.9, 61.5+$y);
    $pdf->write(0, "1. In a new window of Xournal++ click on 'File' > 'Open'.");

    $pdf->SetXY(26.9, 75.0+$y);
    $pdf->write(0, "2. Choose your PDF.");

    $pdf->SetXY(25.7, 88.0+$y);
    $pdf->write(0, "3. Start adding text fields at the desired position.");

    $pdf->SetXY(19.2, 50.2+$y);
    $pdf->write(0, "Follow these  guide to add text to your PDF.  ");

    $pdf->SetXY(18.5, 19.7+$y);
    $pdf->write(0, "Dummy Editor-File");

```
