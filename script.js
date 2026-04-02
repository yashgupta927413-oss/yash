const form = document.getElementById('application-form');
const statusText = document.getElementById('form-status');
const addDetailsChoice = document.getElementById('addDetailsChoice');
const extraDetailsWrap = document.getElementById('extraDetailsWrap');
const extraDetails = document.getElementById('extraDetails');
const scrollProgress = document.getElementById('scroll-progress');
const submissionsBody = document.getElementById('submissionsBody');
const downloadSubmissionsBtn = document.getElementById('downloadSubmissions');

const STORAGE_KEY = 'job_application_submissions';

const readSubmissions = () => {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY)) || [];
  } catch {
    return [];
  }
};

const writeSubmissions = (submissions) => {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(submissions));
};

const renderSubmissions = () => {
  const submissions = readSubmissions();

  if (!submissions.length) {
    submissionsBody.innerHTML = '<tr class="empty-row"><td colspan="6">No submissions yet.</td></tr>';
    return;
  }

  submissionsBody.innerHTML = submissions
    .map(
      (item) => `
      <tr>
        <td>${item.fullName}</td>
        <td>${item.email}</td>
        <td>${item.phone}</td>
        <td>${item.position}</td>
        <td>${item.extraDetails || '-'}</td>
        <td>${new Date(item.submittedAt).toLocaleString()}</td>
      </tr>
    `
    )
    .join('');
};

const onAddDetailsChange = () => {
  const shouldShow = addDetailsChoice.value === 'yes';
  extraDetailsWrap.classList.toggle('hidden', !shouldShow);
  extraDetails.required = shouldShow;
};

addDetailsChoice.addEventListener('change', onAddDetailsChange);
onAddDetailsChange();

window.addEventListener('scroll', () => {
  const pageHeight = document.documentElement.scrollHeight - window.innerHeight;
  const percent = pageHeight > 0 ? (window.scrollY / pageHeight) * 100 : 0;
  scrollProgress.style.width = `${percent}%`;
});

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in-view');
        observer.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.2 }
);

document.querySelectorAll('.reveal').forEach((element) => observer.observe(element));

form.addEventListener('submit', (event) => {
  event.preventDefault();

  if (!form.checkValidity()) {
    statusText.textContent = 'Please complete all required fields.';
    statusText.className = 'error';
    form.reportValidity();
    return;
  }

  const formData = new FormData(form);
  const payload = {
    fullName: formData.get('fullName'),
    email: formData.get('email'),
    phone: formData.get('phone'),
    position: formData.get('position'),
    experience: formData.get('experience'),
    portfolio: formData.get('portfolio'),
    availability: formData.get('availability'),
    extraDetails: formData.get('extraDetails'),
    submittedAt: new Date().toISOString(),
  };

  const existing = readSubmissions();
  existing.unshift(payload);
  writeSubmissions(existing);
  renderSubmissions();

  statusText.textContent = `Thanks, ${payload.fullName}. Your application has been submitted.`;
  statusText.className = 'success';
  form.reset();
  onAddDetailsChange();
});

downloadSubmissionsBtn.addEventListener('click', () => {
  const blob = new Blob([JSON.stringify(readSubmissions(), null, 2)], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;
  link.download = 'job-applications.json';
  link.click();
  URL.revokeObjectURL(url);
});

renderSubmissions();
