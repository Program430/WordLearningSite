
async function mainTable(){
    let lastPageNumber = Number(localStorage.getItem('lastPageNumber')) || 1;
    localStorage.setItem('lastPageNumber', lastPageNumber);
    setPageNumber(lastPageNumber);
    Table.clearTable(); 
    let wordList = await Table.getListFromServer(lastPageNumber);
    Table.addWords(wordList);
    Table.addListenerForEachElement();
}

mainTable();
