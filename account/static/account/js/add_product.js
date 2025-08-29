const input = document.getElementById('id_image')
const preview = document.getElementById('id_preview')

input.style.opacity = 0;
input.addEventListener("change", updateImageDisplay);

function updateImageDisplay() {
    while (preview.firstChild) {
        preview.removeChild(preview.firstChild);
    }

    const curFiles = input.files;
    console.log(curFiles);
  if (curFiles.length === 0) {
    const para = document.createElement("p");
    para.textContent = "No files currently selected for upload";
    preview.appendChild(para);
  } else {
    for (const file of curFiles) {
        const para = document.createElement("p");
        para.textContent = file.name;
        preview.appendChild(para);
        console.log('Element created')
    }
  }
}

const description = document.getElementById('id_description')
function setupAutoResize(description) {
    description.style.overflow = 'hidden';
    description.style.resize = 'none';
    
    function resize() {
        description.style.height = 'auto';
        description.style.height = description.scrollHeight + 'px';
    }
    
    // Начальный ресайз
    resize();
    
    // Ресайз при вводе
    description.addEventListener('input', resize);
    
    // Ресайз при изменении ширины окна
    const resizeObserver = new ResizeObserver(resize);
    resizeObserver.observe(description);
}

// Применение
document.querySelectorAll('description').forEach(setupAutoResize);

