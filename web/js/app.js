const I18N = {
  ru: {
    nav_quotas: 'Квоты и Лимиты',
    nav_models: 'Модели',
    nav_tokens: 'Расход токенов',
    nav_profiles: 'Профили',
    quotas_title: 'Квоты и Скоростные Лимиты',
    quotas_subtitle: 'Прямой опрос Language Server без моков и симуляций',
    weekly_limit: 'Недельный лимит',
    session_limit: 'Сессионный (5 часов)',
    status_safe: 'В норме (Safe)',
    status_available: '100% Доступно',
    status_warning: 'Умеренный расход',
    status_danger: 'Лимит на исходе',
    tile_profile: 'Активный Google профиль',
    tile_tier: 'Тарифный план',
    tile_tokens: 'Токенов израсходовано',
    tile_cache: 'Кэшировано (Экономия)',
    catalog_title: 'Каталог Моделей и Переключение',
    catalog_subtitle: 'Мгновенное переключение модели в IDE и индивидуальные скоростные лимиты',
    filter_all: 'Все модели (14)',
    filter_thinking: 'Thinking (Рассуждающие)',
    search_placeholder: 'Поиск модели по названию (/)...',
    models_count_text: 'моделей',
    tag_active: 'В работе',
    tag_thinking: 'Thinking',
    btn_current_model: 'Текущая модель',
    btn_select_model: 'Выбрать',
    quota_remaining_label: 'Доступный остаток:',
    reset_label: 'Сброс:',
    telemetry_title: 'Телеметрия Токенов («Кто сожрал лимиты»)',
    telemetry_badge: 'Контекст и Вызовы',
    telemetry_subtitle: 'Точный учет входящих, исходящих токенов, рассуждений и кэша по сессиям',
    stat_total: 'Всего токенов',
    stat_input: 'Входящие (Prompt)',
    stat_output: 'Исходящие (Output)',
    stat_thinking: 'Мышление (Thinking)',
    stat_cache: 'Кэш (Context Read)',
    stat_calls: 'API Вызовов',
    dist_title: 'Распределение потребления по моделям',
    dist_subtitle: 'Пропорция токенов',
    th_task: 'Диалог / Задача',
    th_workspace: 'Рабочая папка',
    th_model: 'Модель',
    th_input: 'Входные',
    th_output: 'Выходные',
    th_thinking: 'Мышление',
    th_cache: 'Кэш',
    th_last_active: 'Последняя активность',
    profiles_title: 'Профили и Системное Управление',
    profiles_subtitle: 'Переключение Google аккаунтов, авторизация и перезапуск компонентов',
    accounts_heading: 'Учетные записи Google',
    btn_add_account: 'Добавить Google Аккаунт',
    btn_export_json: 'Экспорт JSON',
    controls_heading: 'Управление процессами',
    ide_status_label: 'Статус Antigravity IDE:',
    status_running: 'Запущен',
    btn_restart_ls: 'Перезапустить Language Server (Сброс RPC)',
    btn_restart_ide: 'Перезапустить Antigravity IDE',
    toast_copied: 'Скопировано в буфер:',
    toast_refreshing: 'Обновление данных...',
    toast_refreshed: 'Данные актуализированы',
    toast_model_switched: 'Модель переключена на',
    toast_account_switched: 'Аккаунт переключен на',
    toast_ls_restarted: 'Language Server успешно перезапущен'
  },
  en: {
    nav_quotas: 'Quotas & Limits',
    nav_models: 'Models',
    nav_tokens: 'Token Telemetry',
    nav_profiles: 'Profiles',
    quotas_title: 'Quotas & Velocity Limits',
    quotas_subtitle: 'Direct Language Server RPC telemetry with zero synthetic data',
    weekly_limit: 'Weekly Limit',
    session_limit: 'Session (5-Hour Window)',
    status_safe: 'Healthy (Safe)',
    status_available: '100% Available',
    status_warning: 'Moderate Usage',
    status_danger: 'Quota Depleted',
    tile_profile: 'Active Google Profile',
    tile_tier: 'Subscription Tier',
    tile_tokens: 'Tokens Burned',
    tile_cache: 'Cached Context (Savings)',
    catalog_title: 'Model Catalog & Quick Switch',
    catalog_subtitle: 'Instant active model switching in IDE and granular velocity limits',
    filter_all: 'All Models (14)',
    filter_thinking: 'Thinking Models',
    search_placeholder: 'Search model by name (/)...',
    models_count_text: 'models',
    tag_active: 'Active',
    tag_thinking: 'Thinking',
    btn_current_model: 'Current Model',
    btn_select_model: 'Select',
    quota_remaining_label: 'Available remaining:',
    reset_label: 'Reset:',
    telemetry_title: 'Token Telemetry (Resource Burn)',
    telemetry_badge: 'Context & Calls',
    telemetry_subtitle: 'Exact breakdown of prompt tokens, completions, reasoning, and cached read',
    stat_total: 'Total Tokens',
    stat_input: 'Prompt (Input)',
    stat_output: 'Completion (Output)',
    stat_thinking: 'Reasoning (Thinking)',
    stat_cache: 'Cached Read',
    stat_calls: 'API Calls',
    dist_title: 'Token Distribution by Model',
    dist_subtitle: 'Token Share',
    th_task: 'Session / Task Title',
    th_workspace: 'Workspace',
    th_model: 'Model',
    th_input: 'Prompt',
    th_output: 'Output',
    th_thinking: 'Thinking',
    th_cache: 'Cached',
    th_last_active: 'Last Activity',
    profiles_title: 'Profiles & System Control',
    profiles_subtitle: 'Google account switching, OAuth authorization, and process resets',
    accounts_heading: 'Google Accounts',
    btn_add_account: 'Add Google Account',
    btn_export_json: 'Export JSON',
    controls_heading: 'Process Control & Diagnostics',
    ide_status_label: 'Antigravity IDE Status:',
    status_running: 'Running',
    btn_restart_ls: 'Restart Language Server (RPC Reset)',
    btn_restart_ide: 'Restart Antigravity IDE',
    toast_copied: 'Copied to clipboard:',
    toast_refreshing: 'Refreshing data...',
    toast_refreshed: 'Data updated successfully',
    toast_model_switched: 'Model switched to',
    toast_account_switched: 'Account switched to',
    toast_ls_restarted: 'Language Server restarted successfully'
  }
};

let currentLang = localStorage.getItem('apogee_lang') || 'ru';

function setLanguage(lang) {
  currentLang = lang;
  localStorage.setItem('apogee_lang', lang);
  document.getElementById('lang-ru').className = 'lang-opt' + (lang === 'ru' ? ' active' : '');
  document.getElementById('lang-en').className = 'lang-opt' + (lang === 'en' ? ' active' : '');

  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (I18N[lang] && I18N[lang][key]) {
      el.textContent = I18N[lang][key];
    }
  });

  const searchInp = document.getElementById('search-models-input');
  if (searchInp) searchInp.placeholder = I18N[lang].search_placeholder;

  renderHeroQuotas();
  renderCatalog();
  renderAccounts();
}

const appState = {
  activeTab: 'quotas',
  activeFilter: 'all',
  searchQuery: '',
  activeEmail: null,
  accounts: [],
  liveQuotas: [],
  quotaSummary: null,
  activeModel: null,
  tier: 'Google AI Pro',
  tokensReport: null,
  lsPid: null,
  lsPort: null
};

function switchTab(tabId, btn) {
  appState.activeTab = tabId;
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  if (btn) btn.classList.add('active');

  document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
  const activePane = document.getElementById('tab-' + tabId);
  if (activePane) activePane.classList.add('active');
}

window.addEventListener('keydown', (e) => {
  if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
  if (e.key === '1') switchTab('quotas', document.querySelectorAll('.tab-btn')[0]);
  else if (e.key === '2') switchTab('catalog', document.querySelectorAll('.tab-btn')[1]);
  else if (e.key === '3') switchTab('tokens', document.querySelectorAll('.tab-btn')[2]);
  else if (e.key === '4') switchTab('accounts', document.querySelectorAll('.tab-btn')[3]);
  else if (e.key.toLowerCase() === 'r') refreshAll();
  else if (e.key === '/') {
    e.preventDefault();
    switchTab('catalog', document.querySelectorAll('.tab-btn')[1]);
    const s = document.getElementById('search-models-input');
    if (s) { s.focus(); s.select(); }
  }
});

function copyValue(val, label) {
  if (!val && val !== 0) return;
  navigator.clipboard.writeText(String(val));
  const t = I18N[currentLang];
  showToast(`${t.toast_copied} ${label} (${val})`);
}

function formatNumber(num) {
  if (!num && num !== 0) return '--';
  if (num >= 1000000) return (num / 1000000).toFixed(2) + 'M';
  if (num >= 1000) return (num / 1000).toFixed(1) + 'K';
  return num.toLocaleString();
}

function formatSeconds(secs) {
  if (!secs || secs <= 0) return '00:00:00';
  const h = Math.floor(secs / 3600);
  const m = Math.floor((secs % 3600) / 60);
  const s = Math.floor(secs % 60);
  return `${String(h).padStart(2, '0')}:${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
}

function showToast(msg) {
  const t = document.getElementById('toast');
  document.getElementById('toast-msg').textContent = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 3200);
}

async function fetchStatus() {
  try {
    const r = await fetch('/api/status');
    const data = await r.json();
    appState.activeEmail = data.activeEmail;
    appState.accounts = data.accounts || [];
    appState.liveQuotas = data.liveQuotas || [];
    appState.quotaSummary = data.quotaSummary || null;
    appState.activeModel = data.activeModel || null;
    appState.tier = data.tier || 'Google AI Pro';
    appState.lsPid = data.lsPid;
    appState.lsPort = data.lsPort;

    renderTopbar();
    renderHeroQuotas();
    renderCatalog();
    renderAccounts();
  } catch (e) {
    document.getElementById('server-status-pill').className = 'status-pill offline';
    document.getElementById('server-status-text').textContent = 'Language Server: Offline';
  }
}

async function fetchTokens() {
  try {
    const r = await fetch('/api/tokens');
    const data = await r.json();
    appState.tokensReport = data;
    renderTelemetry();
  } catch (e) {}
}

async function refreshAll() {
  const t = I18N[currentLang];
  showToast(t.toast_refreshing);
  await Promise.all([fetchStatus(), fetchTokens()]);
  showToast(t.toast_refreshed);
}

function renderTopbar() {
  const pill = document.getElementById('server-status-pill');
  const ptext = document.getElementById('server-status-text');
  if (appState.lsPort) {
    pill.className = 'status-pill';
    ptext.textContent = `Online (:${appState.lsPort})`;
    pill.title = `Language Server PID: ${appState.lsPid}, Port: ${appState.lsPort}`;
  } else {
    pill.className = 'status-pill offline';
    ptext.textContent = 'Offline';
    pill.title = 'Language Server is not responding';
  }

  if (appState.activeModel) {
    const mname = appState.activeModel.name;
    document.getElementById('topbar-model-name').textContent = mname;
    const icon = document.getElementById('topbar-model-icon');
    if (mname.includes('Claude')) icon.src = 'assets/claude.svg';
    else if (mname.includes('GPT')) icon.src = 'assets/openai.svg';
    else icon.src = 'assets/gemini.svg';
  }

  document.getElementById('topbar-email').textContent = appState.activeEmail || (currentLang === 'ru' ? 'Не авторизован' : 'Not logged in');
  const curAcc = appState.accounts.find(a => a.email === appState.activeEmail);
  const avEl = document.getElementById('topbar-avatar');
  if (curAcc && curAcc.picture) {
    avEl.innerHTML = `<img src="${curAcc.picture}" alt="Avatar">`;
  } else {
    avEl.textContent = appState.activeEmail ? appState.activeEmail[0].toUpperCase() : '?';
  }

  document.getElementById('tile-email').textContent = appState.activeEmail || '--';
  document.getElementById('tile-tier').textContent = appState.tier;

  document.getElementById('diag-ls-pid').textContent = appState.lsPid || '--';
  document.getElementById('diag-ls-port').textContent = appState.lsPort || '--';
}

function renderHeroQuotas() {
  const qs = appState.quotaSummary;
  const t = I18N[currentLang];
  if (!qs) return;

  const gem = qs.gemini;
  if (gem) {
    if (gem.weekly) {
      const wpct = gem.weekly.percentage;
      document.getElementById('gemini-w-pct').textContent = `${wpct}%`;
      const bar = document.getElementById('gemini-w-bar');
      bar.style.width = `${Math.min(100, Math.max(0, wpct))}%`;
      if (wpct < 20) bar.className = 'bar-fill danger';
      else if (wpct < 50) bar.className = 'bar-fill warn';
      else bar.className = 'bar-fill gemini';

      const rLoc = gem.weekly.resetTimeLocal ? ` (${gem.weekly.resetTimeLocal})` : '';
      document.getElementById('gemini-w-desc').textContent = `${gem.weekly.description || t.weekly_limit}${rLoc}`;
      document.getElementById('gemini-w-timer').textContent = formatSeconds(gem.weekly.resetSeconds);
    }

    if (gem.session5h) {
      const hpct = gem.session5h.percentage;
      document.getElementById('gemini-5-pct').textContent = `${hpct}%`;
      const bar = document.getElementById('gemini-5-bar');
      bar.style.width = `${Math.min(100, Math.max(0, hpct))}%`;
      if (hpct < 20) bar.className = 'bar-fill danger';
      else if (hpct < 50) bar.className = 'bar-fill warn';
      else bar.className = 'bar-fill gemini';

      const rLoc = gem.session5h.resetTimeLocal ? ` (${gem.session5h.resetTimeLocal})` : '';
      document.getElementById('gemini-5-desc').textContent = `${gem.session5h.description || t.session_limit}${rLoc}`;
      document.getElementById('gemini-5-timer').textContent = formatSeconds(gem.session5h.resetSeconds);
    }

    const pill = document.getElementById('gemini-status-pill');
    const minP = Math.min(gem.weekly?.percentage || 100, gem.session5h?.percentage || 100);
    if (minP < 20) {
      pill.className = 'pill-badge danger';
      pill.textContent = '● ' + t.status_danger;
    } else if (minP < 50) {
      pill.className = 'pill-badge warning';
      pill.textContent = '● ' + t.status_warning;
    } else {
      pill.className = 'pill-badge safe';
      pill.textContent = '● ' + t.status_safe;
    }
  }

  const cl = qs.claudeGpt;
  if (cl) {
    if (cl.weekly) {
      const wpct = cl.weekly.percentage;
      document.getElementById('claude-w-pct').textContent = `${wpct}%`;
      const bar = document.getElementById('claude-w-bar');
      bar.style.width = `${Math.min(100, Math.max(0, wpct))}%`;
      if (wpct < 20) bar.className = 'bar-fill danger';
      else if (wpct < 50) bar.className = 'bar-fill warn';
      else bar.className = 'bar-fill claude';

      const rLoc = cl.weekly.resetTimeLocal ? ` (${cl.weekly.resetTimeLocal})` : '';
      document.getElementById('claude-w-desc').textContent = `${cl.weekly.description || t.weekly_limit}${rLoc}`;
      document.getElementById('claude-w-timer').textContent = formatSeconds(cl.weekly.resetSeconds);
    }

    if (cl.session5h) {
      const hpct = cl.session5h.percentage;
      document.getElementById('claude-5-pct').textContent = `${hpct}%`;
      const bar = document.getElementById('claude-5-bar');
      bar.style.width = `${Math.min(100, Math.max(0, hpct))}%`;
      if (hpct < 20) bar.className = 'bar-fill danger';
      else if (hpct < 50) bar.className = 'bar-fill warn';
      else bar.className = 'bar-fill claude';

      const rLoc = cl.session5h.resetTimeLocal ? ` (${cl.session5h.resetTimeLocal})` : '';
      document.getElementById('claude-5-desc').textContent = `${cl.session5h.description || t.session_limit}${rLoc}`;
      document.getElementById('claude-5-timer').textContent = formatSeconds(cl.session5h.resetSeconds);
    }

    const pill = document.getElementById('claude-status-pill');
    const minP = Math.min(cl.weekly?.percentage || 100, cl.session5h?.percentage || 100);
    if (minP < 20) {
      pill.className = 'pill-badge danger';
      pill.textContent = '● ' + t.status_danger;
    } else if (minP < 50) {
      pill.className = 'pill-badge warning';
      pill.textContent = '● ' + t.status_warning;
    } else {
      pill.className = 'pill-badge safe';
      pill.textContent = '● ' + t.status_available;
    }
  }
}

function filterCatalog(f, btn) {
  appState.activeFilter = f;
  document.querySelectorAll('.filter-chip').forEach(b => b.classList.remove('active'));
  if (btn) btn.classList.add('active');
  renderCatalog();
}

function onSearchInput(val) {
  appState.searchQuery = val;
  renderCatalog();
}

function renderCatalog() {
  const container = document.getElementById('models-container');
  const t = I18N[currentLang];
  let models = appState.liveQuotas || [];

  document.getElementById('tab-models-count').textContent = models.length;
  document.getElementById('models-count-badge').textContent = `${models.length} ${t.models_count_text}`;

  if (appState.activeFilter === 'claude') {
    models = models.filter(m => m.brand === 'claude');
  } else if (appState.activeFilter === 'openai') {
    models = models.filter(m => m.brand === 'openai');
  } else if (appState.activeFilter === 'gemini') {
    models = models.filter(m => m.brand === 'gemini');
  } else if (appState.activeFilter === 'thinking') {
    models = models.filter(m => m.isThinking);
  }

  if (appState.searchQuery.trim()) {
    const q = appState.searchQuery.toLowerCase();
    models = models.filter(m => m.name.toLowerCase().includes(q) || (m.modelId && m.modelId.toLowerCase().includes(q)));
  }

  if (models.length === 0) {
    container.innerHTML = `<div style="grid-column: 1 / -1; text-align: center; padding: 40px; color: var(--text-muted);">${currentLang === 'ru' ? 'Модели не найдены.' : 'No models found.'}</div>`;
    return;
  }

  const activeName = appState.activeModel?.name;

  container.innerHTML = models.map(m => {
    const isActive = (activeName && activeName === m.name);
    const pct = m.percentage;
    let barClass = 'bar-fill ' + m.brand;
    let numColor = '#fff';

    if (pct < 20) { barClass = 'bar-fill danger'; numColor = '#fb7185'; }
    else if (pct < 50) { barClass = 'bar-fill warn'; numColor = '#fbbf24'; }

    const grpName = m.groupKey === 'claudeGpt' ? (currentLang === 'ru' ? 'Квота Claude/GPT' : 'Claude/GPT Quota Pool') : (currentLang === 'ru' ? 'Квота Gemini' : 'Gemini Quota Pool');

    return `
      <div class="model-card ${isActive ? 'active-model' : ''}">
        <div class="model-card-top">
          <div class="model-logo">
            <img src="${m.icon}" alt="${m.provider}">
          </div>
          <div class="model-info">
            <div class="model-name" title="${m.name}">
              ${m.name}
              ${isActive ? `<span class="tag-active">${t.tag_active}</span>` : ''}
              ${m.isThinking ? `<span class="tag-thinking">${t.tag_thinking}</span>` : ''}
            </div>
            <div class="model-meta">
              <span>${m.provider}</span>
              <span>•</span>
              <span>${grpName}</span>
            </div>
          </div>
        </div>

        <div class="model-quota-wrap">
          <div class="model-quota-stats">
            <span style="font-size:11px; color:var(--text-muted);">${t.quota_remaining_label}</span>
            <span class="model-pct" style="color:${numColor};">${pct}%</span>
          </div>
          <div class="bar-container">
            <div class="${barClass}" style="width: ${pct}%;"></div>
          </div>
        </div>

        <div class="model-card-footer">
          <span>${t.reset_label} ${m.resetTimeLocal ? m.resetTimeLocal : (currentLang === 'ru' ? 'В норме' : 'Ready')}</span>
          ${isActive
            ? `<button class="btn-select-model is-current">${t.btn_current_model}</button>`
            : `<button class="btn-select-model" onclick="selectModel('${m.modelId}', '${m.name}')">${t.btn_select_model}</button>`
          }
        </div>
      </div>
    `;
  }).join('');
}

async function selectModel(mid, mname) {
  const t = I18N[currentLang];
  try {
    const r = await fetch('/api/select_model', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ modelId: mid, name: mname })
    });
    const res = await r.json();
    if (res.success) {
      showToast(`${t.toast_model_switched} ${mname}`);
      await fetchStatus();
    } else {
      showToast('Error: ' + (res.error || 'Failed'));
    }
  } catch (e) {
    showToast('Network error');
  }
}

function renderTelemetry() {
  const rep = appState.tokensReport;
  if (!rep) return;

  document.getElementById('tile-tokens').textContent = formatNumber(rep.totalTokens);
  document.getElementById('tile-cache').textContent = formatNumber(rep.totalCacheTokens);

  document.getElementById('t-total').textContent = formatNumber(rep.totalTokens);
  document.getElementById('t-input').textContent = formatNumber(rep.totalInputTokens);
  document.getElementById('t-output').textContent = formatNumber(rep.totalOutputTokens);
  document.getElementById('t-thinking').textContent = formatNumber(rep.totalThinkingTokens);
  document.getElementById('t-cache').textContent = formatNumber(rep.totalCacheTokens);
  document.getElementById('t-calls').textContent = rep.totalCalls.toLocaleString();

  const modelsSummary = rep.modelsSummary || {};
  const barEl = document.getElementById('dist-bar');
  const legendEl = document.getElementById('dist-legend');

  const colors = ['#00f2fe', '#8b5cf6', '#f59e0b', '#10b981', '#f43f5e', '#ec4899'];
  let segs = [];
  let legendItems = [];
  let i = 0;

  for (const [mname, data] of Object.entries(modelsSummary)) {
    const c = colors[i % colors.length];
    const share = rep.totalTokens > 0 ? (data.total / rep.totalTokens * 100).toFixed(1) : 0;
    segs.push(`<div class="dist-seg" style="width:${share}%; background:${c};" title="${mname}: ${share}% (${formatNumber(data.total)})"></div>`);
    legendItems.push(`<span style="display:inline-flex; align-items:center; gap:5px;"><span style="width:8px; height:8px; border-radius:50%; background:${c};"></span>${mname} (${share}%)</span>`);
    i++;
  }

  barEl.innerHTML = segs.join('');
  legendEl.innerHTML = legendItems.join('');

  const tbody = document.getElementById('sessions-tbody');
  const convs = rep.conversations || [];

  if (convs.length === 0) {
    tbody.innerHTML = `<tr><td colspan="8" style="text-align:center; padding:32px; color:var(--text-muted);">${currentLang === 'ru' ? 'Нет зарегистрированных сессий.' : 'No registered sessions.'}</td></tr>`;
    return;
  }

  tbody.innerHTML = convs.map(c => {
    let modelBadges = [];
    for (const [mname, mstats] of Object.entries(c.models || {})) {
      let icon = 'assets/gemini.svg';
      if (mname.includes('Claude')) icon = 'assets/claude.svg';
      else if (mname.includes('GPT')) icon = 'assets/openai.svg';
      modelBadges.push(`<span style="display:inline-flex; align-items:center; gap:4px; margin-right:6px;"><img src="${icon}" style="width:14px; height:14px; border-radius:3px;">${mname}</span>`);
    }

    return `
      <tr>
        <td>
          <div class="session-title" title="${c.title}">${c.title}</div>
        </td>
        <td>
          <div class="session-ws">${c.workspace}</div>
        </td>
        <td>
          <div style="font-size:11px;">${modelBadges.join('')}</div>
        </td>
        <td class="num-mono">${formatNumber(c.totalInputTokens)}</td>
        <td class="num-mono">${formatNumber(c.totalOutputTokens)}</td>
        <td class="num-mono">${formatNumber(c.totalThinkingTokens)}</td>
        <td class="num-mono" style="color:#34d399;">${formatNumber(c.totalCacheTokens)}</td>
        <td>
          <div class="rel-time">${c.lastModifiedTime}</div>
        </td>
      </tr>
    `;
  }).join('');
}

function renderAccounts() {
  const container = document.getElementById('accounts-list');
  const accounts = appState.accounts || [];

  if (accounts.length === 0) {
    container.innerHTML = `<div style="text-align:center; padding:20px; color:var(--text-muted);">${currentLang === 'ru' ? 'Нет сохраненных аккаунтов.' : 'No saved accounts.'}</div>`;
    return;
  }

  container.innerHTML = accounts.map(acc => {
    const isActive = (acc.email === appState.activeEmail);
    return `
      <div class="acc-item ${isActive ? 'is-active' : ''}">
        <div class="acc-left">
          <div class="acc-avatar">
            ${acc.picture ? `<img src="${acc.picture}">` : (acc.email ? acc.email[0].toUpperCase() : '?')}
          </div>
          <div>
            <div class="acc-email">${acc.email}</div>
            <div class="acc-tier">${acc.tier || 'Google AI Pro'} • ${isActive ? '<span style="color:#00f2fe; font-weight:700;">' + (currentLang === 'ru' ? 'Активен' : 'Active') + '</span>' : (currentLang === 'ru' ? 'Резервный' : 'Standby')}</div>
          </div>
        </div>

        <div>
          ${isActive
            ? `<span style="font-size:12px; color:#34d399; font-weight:700;">● ${currentLang === 'ru' ? 'Текущий' : 'Current'}</span>`
            : `<button class="btn-action-secondary" onclick="switchAccount('${acc.email}')" style="padding:4px 10px; font-size:11px;">${currentLang === 'ru' ? 'Переключить' : 'Switch'}</button>`
          }
        </div>
      </div>
    `;
  }).join('');
}

async function switchAccount(email) {
  const t = I18N[currentLang];
  try {
    const r = await fetch('/api/switch', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email: email })
    });
    const res = await r.json();
    if (res.success) {
      showToast(`${t.toast_account_switched} ${email}`);
      await fetchStatus();
    } else {
      showToast('Error: ' + (res.error || 'Failed'));
    }
  } catch (e) {
    showToast('Network error');
  }
}

async function startOAuth() {
  try {
    const r = await fetch('/api/oauth/start');
    const data = await r.json();
    if (data.auth_url) {
      window.open(data.auth_url, '_blank');
      showToast(currentLang === 'ru' ? 'Окно авторизации Google открыто' : 'Google Auth opened in new tab');
    }
  } catch (e) {
    showToast('OAuth error');
  }
}

function exportAccounts() {
  window.location.href = '/api/export_accounts';
}

async function restartLanguageServer() {
  const t = I18N[currentLang];
  showToast('Restarting Language Server...');
  try {
    const r = await fetch('/api/restart_ls');
    const data = await r.json();
    if (data.success) {
      showToast(t.toast_ls_restarted);
      setTimeout(refreshAll, 1500);
    } else {
      showToast('Restart failed');
    }
  } catch (e) {
    showToast('Network error');
  }
}

async function restartIDE() {
  const msg = currentLang === 'ru' ? 'Перезапустить Antigravity IDE? Открытые файлы будут сохранены.' : 'Restart Antigravity IDE? Open files will be preserved.';
  if (!confirm(msg)) return;
  showToast('Restarting IDE...');
  try {
    await fetch('/api/restart_ide');
    showToast(currentLang === 'ru' ? 'Команда перезапуска IDE отправлена' : 'IDE restart command sent');
  } catch (e) {
    showToast('Error');
  }
}

setInterval(() => {
  const qs = appState.quotaSummary;
  if (!qs) return;

  if (qs.gemini?.weekly?.resetSeconds > 0) {
    qs.gemini.weekly.resetSeconds--;
    const el = document.getElementById('gemini-w-timer');
    if (el) el.textContent = formatSeconds(qs.gemini.weekly.resetSeconds);
  }
  if (qs.gemini?.session5h?.resetSeconds > 0) {
    qs.gemini.session5h.resetSeconds--;
    const el = document.getElementById('gemini-5-timer');
    if (el) el.textContent = formatSeconds(qs.gemini.session5h.resetSeconds);
  }

  if (qs.claudeGpt?.weekly?.resetSeconds > 0) {
    qs.claudeGpt.weekly.resetSeconds--;
    const el = document.getElementById('claude-w-timer');
    if (el) el.textContent = formatSeconds(qs.claudeGpt.weekly.resetSeconds);
  }
  if (qs.claudeGpt?.session5h?.resetSeconds > 0) {
    qs.claudeGpt.session5h.resetSeconds--;
    const el = document.getElementById('claude-5-timer');
    if (el) el.textContent = formatSeconds(qs.claudeGpt.session5h.resetSeconds);
  }
}, 1000);

setInterval(() => {
  fetchStatus();
  fetchTokens();
}, 10000);

window.addEventListener('DOMContentLoaded', () => {
  setLanguage(currentLang);
  const params = new URLSearchParams(window.location.search);
  const tab = params.get('tab');
  if (tab) {
    const btn = document.querySelector(`.tab-btn[onclick*="${tab}"]`);
    switchTab(tab, btn);
  }
  fetchStatus();
  fetchTokens();
});
