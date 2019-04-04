find . -maxdepth 1 -mindepth 1 -type d | while read line; do
        trimmed="$(echo $line | cut -d'/' -f2)"
        path="/tmp/$trimmed"
        cp -r $line $path

done
