var textarea1 = document.getElementById("txtBox2");
var wordCount = document.getElementById("word-count");
var charCount = document.getElementById("charac-count");

textarea1.addEventListener("input", function() {
  var words = this.value.split(/\s+/);
  var characters = this.value.replace(/\s+/g, "");
  wordCount.textContent = words.length;
  charCount.textContent = characters.length;
});