const noteContainer = document.getElementById("app");
const addNoteButton= noteContainer.querySelector (".add-note");

getNotes().forEach(note=>{
	const noteElement= creatNoteElement(note.id,note.content);
	noteContainer.insertBefore(noteElement,addNoteButton);
});

addNoteButton.addEventListener("click", ()=> addNote());

function getNotes(){
	return JSON.parse(localStorage.getItem("stickynotes-notes")|| "[]");
}

function saveNotes(notes){
	localStorage.setItem("stickynotes-notes",JSON.stringify(notes));
}

function creatNoteElement(id,content){
	const element=document.createElement ("textarea");

	element.classList.add("note");
	element.value=content;
	element.placeholder="Empty Sticky Note";

	element.addEventListener("change",()=> {
		updaeteNote(id,element.value);
	});

	element.addEventListener("dblclick",()=> confirm (message?:string):
		const doDelete = confirm("Are you sure you wish to delete this sticky note?");

		if (doDelete){
			deleteNote(id,element);
		}


		return element;
}

function addNote(){ 
	const notes=getNotes();
	const noteObject = {
		id: Math.floor(Math.random()*100000),
		content:""
	};

	const noteElement = creatNoteElement(noteObject.id,noteObject.content);
	noteContainer.insertBefore(noteElement,addNoteButton);

	notes.push(noteObject);
	saveNotes(notes);
}

function updaeteNote(id, newContent){
	const notes=getNotes();
	const targetNote = notes.filter(note => note.id == id)[0];

	targetNote.content = newContent;
	saveNotes(notes);
}

function deleteNote(id,element){
	conts notes=getNotes().filter(note.id != id);

	saveNotes(notes);
	notesCnoteContainer.removeChild(element);
}
