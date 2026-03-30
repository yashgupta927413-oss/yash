(function () {
  function getCookie(name) {
    const cookies = document.cookie ? document.cookie.split(';') : [];
    for (const cookieRaw of cookies) {
      const cookie = cookieRaw.trim();
      if (cookie.startsWith(name + '=')) {
        return decodeURIComponent(cookie.slice(name.length + 1));
      }
    }
    return '';
  }

  function initDragSort() {
    const handles = document.querySelectorAll('.drag-handle');
    if (!handles.length) return;

    const tbody = document.querySelector('#result_list tbody');
    if (!tbody) return;

    const reorderUrl = handles[0].dataset.reorderUrl;
    if (!reorderUrl) return;

    let draggingRow = null;

    tbody.querySelectorAll('tr').forEach((row) => {
      row.setAttribute('draggable', 'true');

      row.addEventListener('dragstart', () => {
        draggingRow = row;
        row.classList.add('dragging-row');
      });

      row.addEventListener('dragend', () => {
        row.classList.remove('dragging-row');
        draggingRow = null;
        const ids = Array.from(tbody.querySelectorAll('tr'))
          .map((tr) => tr.id.split('-').pop())
          .map((id) => Number(id))
          .filter((id) => !Number.isNaN(id));

        fetch(reorderUrl, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
          },
          body: JSON.stringify({ ids }),
        }).catch(() => {
          // keep UI responsive even if save fails
        });
      });

      row.addEventListener('dragover', (event) => {
        event.preventDefault();
        if (!draggingRow || draggingRow === row) return;
        const rect = row.getBoundingClientRect();
        const offset = event.clientY - rect.top;
        const shouldInsertBefore = offset < rect.height / 2;
        if (shouldInsertBefore) {
          tbody.insertBefore(draggingRow, row);
        } else {
          tbody.insertBefore(draggingRow, row.nextSibling);
        }
      });
    });
  }

  window.addEventListener('load', initDragSort);
})();
