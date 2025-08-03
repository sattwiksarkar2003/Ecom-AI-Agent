function triggerVoiceSearch() {

    alert("Cliced voice search button. This feature is not yet implemented.");

  fetch("/voice_search")
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        document.getElementById("searchBox").value = data.text;
      } else {
        alert("❌ Error: " + data.error);
      }
    })
    .catch(error => {
      alert("⚠️ Could not connect to backend.");
      console.error(error);
    });
}
