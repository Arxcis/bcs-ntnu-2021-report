set -o pipefail
set -e

declare -a CHAPTERS=("introduction" "development process" "functional requirements" "user interface" "architecture" "results" "discussion" "conclusion")


i=1
for CHAPTER in "${CHAPTERS[@]}";
do
    echo $CHAPTER

    # Create filepaths
    CHAPTER_TEX=$(echo "chapters/$i-$CHAPTER.tex" | sed 's/ /-/g')
    CHAPTER_MD=$(find markdown -maxdepth 2 -mindepth 2 -iname "$CHAPTER*.md")
    CHAPTER_FOLDER=$(echo $CHAPTER_MD | sed 's/.md//g')

    # Copy image folder
    cp -r "$CHAPTER_FOLDER" chapters/ 2>/dev/null || true # Fail silently

    # Pandoc
    pandoc\
        --from markdown\
        --to latex\
        --listings\
        "$CHAPTER_MD" > "$CHAPTER_TEX"

    # Python to string replace
    python3 markdown-to-latex.py "$CHAPTER_TEX"

    i=$((i+1))
done