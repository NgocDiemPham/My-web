# project structure
# myproject/
# ├── app.py
# ├── templates/
# │   └── index.html
# └── static/
#     └── css/
#         └── style.css

# =========================
# file: app.py
# =========================
from flask import Flask, render_template, request

app = Flask(__name__)

NAV_ITEMS = [
    {"label": "Lobby", "href": "#home"},
    {"label": "Projects", "href": "#project"},
    {"label": "Goals", "href": "#objectives"},
    {"label": "Findings", "href": "#features"},
    {"label": "Partners", "href": "#partners"},
    {"label": "Contact", "href": "#contact"},
]

OBJECTIVES = [
    {
        "title": "Revitalize Vietnamese folk rhymes for younger generations",
        "text": "By turning them into a more exciting and accessible digital experience, especially through games.",
        "icon": "💡",
    },
    {
        "title": "Preserve Vietnam’s intangible cultural heritage",
        "text": "By reintroducing folk rhymes into modern cultural life instead of letting them fade from common use.",
        "icon": "❤️",
    },
    {
        "title": "Build an interactive mystery/puzzle experience",
        "text": "That combines folk culture with AI technology. This is the project’s central creative goal.",
        "icon": "📚",
    },
    {
        "title": "Test how OCR and LLMs help decode damaged handwritten texts",
        "text": "Especially in a detective-style investigation setting.",
        "icon": "🤝",
    },
    {
        "title": "Explore the effect of AI errors or hallucinations",
        "text": "On interpretation and decision-making in the investigation process. The gap between the original text and AI output is treated as part of the narrative tension.",
        "icon": "🧑‍🏫",
    },
    {
        "title": "Develop the author’s academic and research skills",
        "text": "While also deepening understanding of folk language, emotion, and human expression as preparation for a future path in psychology and counseling.",
        "icon": "🌍",
    },
]

TARGET_GROUPS = [
    {
        "title": "Young people / the digital generation",
        "text": "We see them as a main target because folk rhymes are becoming less familiar to younger generations, so we want to bring this heritage back to them in a form that feels exciting and relevant today.",
    },
    {
        "title": "Children",
        "text": "We include children as a target because the project uses digital games, which we describe as one of the most familiar and influential mediums for children today.",
    },
    {
        "title": "People interested in AI and language analysis",
        "text": "We see them as a target because the project explores how OCR and LLMs interpret damaged texts, and how AI mistakes can affect the investigation process.",
    },
 {
        "title": "Players who enjoy mystery and puzzle-solving",
        "text": "We target this group because the whole project is designed as an interactive detective experience where players solve a case by interpreting fragmented clues from folk rhymes.",
    },
 {
        "title": "People interested in Vietnamese folk culture",
        "text": "We target this audience because we treat folk rhymes as a form of cultural code and want to preserve and revitalize this intangible cultural heritage in a meaningful way.",
    },
 {
        "title": "Academic or research-oriented audiences",
        "text": "We also target students, researchers, or educators because the project is framed as an in-depth exploration of folk language, cultural meaning, and research practice.",
    },

]

FEATURES = [
    "Research Question",
    "Struggles",
    "AI tools' generation and comparison",
    "The whole process of delivering",
    "Human Reflection",
    "Reference in here",
]

PARTNERS = [
    {"name": "Phạm Ngọc Diễm", "country": "Web designer and Content/Game Creator", "type": "25diem.pn@vinuni.edu.vn"},
    {"name": "Lê Trương Bảo Hân", "country": "Content/Game Creator and Researcher", "type": "25han.ltb@vinuni.edu.vn"},
    {"name": "Nguyễn Tiến Đạt", "country": "Game Development Assisstant", "type": "25dat.nt@vinuni.edu.vn"},
    {"name": "Gordon Huynh & Nguyễn Trần Xuân Bách", "country": "Helping with Game Content", "type": "25gordon.h@vinuni.edu.vn & 25bach.ntx@vinuni.edu.vn"},
]

@app.route("/", methods=["GET", "POST"])
def home():
    success_message = ""
    form_data = {"name": "", "email": "", "message": ""}

    if request.method == "POST":
        form_data = {
            "name": request.form.get("name", "").strip(),
            "email": request.form.get("email", "").strip(),
            "message": request.form.get("message", "").strip(),
        }

        if all(form_data.values()):
            success_message = "Mail sent successfully."
            form_data = {"name": "", "email": "", "message": ""}
        else:
            success_message = "Please fill in your full name, email address, and message content."

    return render_template(
        "index.html",
        nav_items=NAV_ITEMS,
        objectives=OBJECTIVES,
        target_groups=TARGET_GROUPS,
        features=FEATURES,
        partners=PARTNERS,
        success_message=success_message,
        form_data=form_data,
    )

if __name__ == "__main__":
    app.run(debug=True)


# =========================
# file: templates/index.html
# =========================
"""
<!doctype html>
<html lang="vi">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Dự án Digital Humanities</title>
    <meta name="description" content="Website Designed by Flask">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <header class="site-header">
        <div class="container nav-wrap">
            <a href="#home" class="brand">
                <span class="brand-mark">DH</span>
                <span class="brand-text">Digital Humanities Project</span>
            </a>

            <nav class="main-nav">
                {% for item in nav_items %}
                    <a href="{{ item.href }}">{{ item.label }}</a>
                {% endfor %}
            </nav>

            <a class="nav-cta" href="#contact">Join us</a>
        </div>
    </header>

    <main>
        <section id="home" class="hero">
            <div class="container hero-grid">
                <div class="hero-copy">
                    <span class="eyebrow"> Digital Humanities Project from S1.3C team</span>
                    <h1>We turn insights into impacts</h1>
                    <p class="hero-text">
                        An AI-generated website with human supervision
                    </p>

                    <div class="hero-actions">
                        <a class="btn btn-primary" href="#project">Discover the project</a>
                        <a class="btn btn-secondary" href="#contact">Contact</a>
                    </div>

                    <div class="hero-points">
                        <div class="point">
                            <strong>Vietnamese Current Problems</strong>
                            <span>Traditional folk rhymes are becoming less familiar to younger generations in Vietnam. As digital entertainment grows, many children and young people no longer engage with these cultural materials in everyday life. This creates a risk that an important part of Vietnam’s intangible cultural heritage will gradually fade from cultural memory.</span>
                        </div>
                        <div class="point">
                            <strong>Solutions</strong>
                            <span>We aim to revive folk rhymes by transforming them into an interactive digital mystery game. By combining Vietnamese folk culture with AI technologies such as OCR and LLMs, we make traditional heritage more engaging, accessible, and relevant to the digital generation. This approach both preserves cultural values and connects them with modern innovation.</span>
                        </div>
                        <div class="point">
                            <strong>Duties</strong>
                            <span>Our duty is to preserve and promote Vietnamese traditional cultural values in ways that fit the modern era. We also have the responsibility to use AI carefully and critically, recognizing its limits and ensuring that human interpretation remains important, especially when dealing with cultural meaning and authenticity.</span>
                        </div>
                    </div>
                </div>

                <div class="hero-card">
                    <div class="glass-card">
                        <h2>Brief Introduction</h2>
                        <p>
                           We are VinUniversity students majoring in Psychology in the College of Arts and Sciences, with a strong desire to contribute to our community and society. This project represents a small but meaningful step in our effort to preserve Vietnam’s intangible cultural heritage in the digital age. 

                        </p>
                        <ul>
                            <li>Tài nguyên học tập mở</li>
                            <li>Hoạt động cho lớp học</li>
                            <li>Hỗ trợ giáo viên và gia đình</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <section id="project" class="section">
            <div class="container">
                <div class="section-heading">
                    <span class="section-tag">About this project</span>
                    <h2>Folk Rhymes – The Cultural Identity of the Vietnamese Nation</h2>
                    <p>
                        This is a non-profit project aimed at building a future enriched with traditional values alongside the development of AI. In this way, it both preserves traditional values and keeps pace with the digital age.
                    </p>
                </div>

                <div class="about-grid">
                    <article class="about-card">
                        <h3>Our Duties</h3>
                        <p>
                            Giúp học sinh phát triển tư duy số, ý thức công dân số và kỹ năng
                            cảm xúc - xã hội thông qua các hoạt động học tập có ý nghĩa.
                        </p>
                    </article>
                    <article class="about-card">
                        <h3>Vietnamese Current Problems</h3>
                        <p>
                            Công nghệ thường được dùng để giải trí nhiều hơn học tập; học sinh cần
                            được hướng dẫn để sử dụng công cụ số một cách an toàn và đúng mục đích.
                        </p>
                    </article>
                    <article class="about-card">
                        <h3>Solutions</h3>
                        <p>
                            Tạo một hệ sinh thái tài nguyên và hoạt động để giáo viên, học sinh
                            và gia đình cùng tham gia trong một môi trường chung.
                        </p>
                    </article>
                </div>
            </div>
        </section>

        <section id="objectives" class="section section-alt">
            <div class="container">
                <div class="section-heading">
                    <span class="section-tag">Goals</span>
                    <h2>We aim to</h2>
                </div>

                <div class="card-grid">
                    {% for item in objectives %}
                    <article class="info-card">
                        <div class="icon">{{ item.icon }}</div>
                        <h3>{{ item.title }}</h3>
                        <p>{{ item.text }}</p>
                    </article>
                    {% endfor %}
                </div>
            </div>
        </section>

        <section class="section">
            <div class="container">
                <div class="section-heading">
                    <span class="section-tag">Target audience</span>
                    <h2>For who?</h2>
                </div>

                <div class="audience-grid">
                    {% for item in target_groups %}
                    <article class="audience-card">
                        <h3>{{ item.title }}</h3>
                        <p>{{ item.text }}</p>
                    </article>
                    {% endfor %}
                </div>
            </div>
        </section>

        <section id="features" class="section section-alt">
            <div class="container">
                <div class="section-heading">
                    <span class="section-tag">Tinh nang</span>
                    <h2>Điểm nổi bật của nền tảng</h2>
                </div>

                <div class="features-box">
                    {% for feature in features %}
                    <div class="feature-row">
                        <span class="check">✓</span>
                        <p>{{ feature }}</p>
                    </div>
                    {% endfor %}
                </div>
            </div>
        </section>

        <section id="partners" class="section">
            <div class="container">
                <div class="section-heading">
                    <span class="section-tag">Resources</span>
                    <h2>Reference</h2>
                    <p>
                        Shoutout to those helping us with designing this project.
                    </p>
                </div>

                <div class="partners-grid">
                    {% for partner in partners %}
                    <article class="partner-card">
                        <div class="partner-badge">{{ partner.country }}</div>
                        <h3>{{ partner.name }}</h3>
                        <p>{{ partner.type }}</p>
                    </article>
                    {% endfor %}
                </div>
            </div>
        </section>

        <section id="contact" class="section section-alt">
            <div class="container contact-grid">
                <div>
                    <div class="section-heading left">
                        <span class="section-tag">About us</span>
                        <h2>Connect with us</h2>
                        <p>
                            Đây là form mẫu. Hiện tại nó chỉ hiển thị thông báo thành công,
                            chưa gửi email thật.
                        </p>
                    </div>
                </div>

                <form class="contact-form" method="post">
                    {% if success_message %}
                        <div class="form-alert">{{ success_message }}</div>
                    {% endif %}

                    <label for="name">Name</label>
                    <input id="name" name="name" type="text" value="{{ form_data.name }}" required>

                    <label for="email">Email</label>
                    <input id="email" name="email" type="email" value="{{ form_data.email }}" required>

                    <label for="message">Questions for us</label>
                    <textarea id="message" name="message" rows="5" required>{{ form_data.message }}</textarea>

                    <button type="submit" class="btn btn-primary btn-full">Send contact</button>
                </form>
            </div>
        </section>
    </main>

    <footer class="site-footer">
        <div class="container footer-wrap">
            <div>
                <strong>Digital Humanities Project</strong>
                <p>Website designed by Flask</p>
            </div>
            <div>
                <p>© 2026 - Demo by Code Copilot</p>
            </div>
        </div>
    </footer>
</body>
</html>
"""

# =========================
# file: static/css/style.css
# =========================
"""
:root {
    --bg: #f5f7fb;
    --bg-alt: #edf2f8;
    --surface: #ffffff;
    --surface-soft: rgba(255, 255, 255, 0.72);
    --text: #172033;
    --muted: #61708a;
    --line: #d9e2ef;
    --primary: #1d4ed8;
    --primary-dark: #163ea8;
    --accent: #0f766e;
    --shadow: 0 18px 50px rgba(23, 32, 51, 0.10);
    --radius: 22px;
    --radius-sm: 16px;
    --container: 1180px;
}

* {
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    margin: 0;
    font-family: Arial, Helvetica, sans-serif;
    color: var(--text);
    background: var(--bg);
    line-height: 1.6;
}

a {
    color: inherit;
    text-decoration: none;
}

.container {
    width: min(var(--container), calc(100% - 32px));
    margin: 0 auto;
}

.site-header {
    position: sticky;
    top: 0;
    z-index: 100;
    backdrop-filter: blur(12px);
    background: rgba(245, 247, 251, 0.82);
    border-bottom: 1px solid rgba(217, 226, 239, 0.9);
}

.nav-wrap {
    min-height: 76px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
}

.brand {
    display: inline-flex;
    align-items: center;
    gap: 12px;
    font-weight: 700;
}

.brand-mark {
    width: 42px;
    height: 42px;
    display: grid;
    place-items: center;
    border-radius: 12px;
    background: linear-gradient(135deg, var(--primary), var(--accent));
    color: #fff;
    box-shadow: var(--shadow);
}

.brand-text {
    font-size: 1rem;
}

.main-nav {
    display: flex;
    align-items: center;
    gap: 20px;
    flex-wrap: wrap;
}

.main-nav a {
    color: var(--muted);
    font-weight: 600;
}

.main-nav a:hover {
    color: var(--text);
}

.nav-cta,
.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    border-radius: 999px;
    font-weight: 700;
    transition: 0.2s ease;
}

.nav-cta {
    padding: 12px 18px;
    background: var(--text);
    color: #fff;
}

.nav-cta:hover {
    opacity: 0.92;
}

.hero {
    padding: 92px 0 56px;
    background:
        radial-gradient(circle at top left, rgba(29, 78, 216, 0.14), transparent 26%),
        radial-gradient(circle at right center, rgba(15, 118, 110, 0.12), transparent 24%),
        linear-gradient(180deg, #f9fbff 0%, #eff4fb 100%);
}

.hero-grid {
    display: grid;
    grid-template-columns: 1.15fr 0.85fr;
    gap: 32px;
    align-items: center;
}

.eyebrow,
.section-tag {
    display: inline-block;
    padding: 8px 14px;
    border-radius: 999px;
    background: rgba(29, 78, 216, 0.10);
    color: var(--primary);
    font-weight: 700;
    font-size: 0.92rem;
}

.hero h1 {
    margin: 18px 0 16px;
    font-size: clamp(2.4rem, 5vw, 4.4rem);
    line-height: 1.08;
    max-width: 12ch;
}

.hero-text {
    max-width: 62ch;
    font-size: 1.06rem;
    color: var(--muted);
}

.hero-actions {
    display: flex;
    gap: 14px;
    flex-wrap: wrap;
    margin: 28px 0 34px;
}

.btn {
    padding: 14px 22px;
    border: 0;
    cursor: pointer;
}

.btn-primary {
    background: var(--primary);
    color: #fff;
}

.btn-primary:hover {
    background: var(--primary-dark);
}

.btn-secondary {
    background: #fff;
    color: var(--text);
    border: 1px solid var(--line);
}

.btn-secondary:hover {
    background: #f8fbff;
}

.btn-full {
    width: 100%;
}

.hero-points {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 14px;
}

.point {
    padding: 16px;
    border-radius: var(--radius-sm);
    background: rgba(255, 255, 255, 0.72);
    border: 1px solid rgba(217, 226, 239, 0.9);
}

.point strong {
    display: block;
    margin-bottom: 4px;
    font-size: 1rem;
}

.point span {
    color: var(--muted);
    font-size: 0.95rem;
}

.hero-card {
    display: flex;
    justify-content: center;
}

.glass-card {
    width: 100%;
    padding: 28px;
    border-radius: 28px;
    background: var(--surface-soft);
    border: 1px solid rgba(255, 255, 255, 0.7);
    box-shadow: var(--shadow);
}

.glass-card h2 {
    margin-top: 0;
}

.glass-card ul {
    margin: 18px 0 0;
    padding-left: 20px;
}

.section {
    padding: 84px 0;
}

.section-alt {
    background: var(--bg-alt);
}

.section-heading {
    max-width: 760px;
    margin: 0 auto 34px;
    text-align: center;
}

.section-heading.left {
    margin-left: 0;
    text-align: left;
}

.section-heading h2 {
    margin: 14px 0 12px;
    font-size: clamp(1.9rem, 3vw, 3rem);
    line-height: 1.15;
}

.section-heading p {
    color: var(--muted);
    margin: 0;
}

.about-grid,
.card-grid,
.audience-grid,
.partners-grid {
    display: grid;
    gap: 20px;
}

.about-grid {
    grid-template-columns: repeat(3, 1fr);
}

.card-grid {
    grid-template-columns: repeat(3, 1fr);
}

.audience-grid {
    grid-template-columns: repeat(3, 1fr);
}

.partners-grid {
    grid-template-columns: repeat(4, 1fr);
}

.about-card,
.info-card,
.audience-card,
.partner-card,
.contact-form {
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: var(--radius);
    box-shadow: var(--shadow);
}

.about-card,
.info-card,
.audience-card,
.partner-card {
    padding: 24px;
}

.info-card .icon {
    width: 54px;
    height: 54px;
    display: grid;
    place-items: center;
    border-radius: 16px;
    background: rgba(29, 78, 216, 0.10);
    font-size: 1.5rem;
    margin-bottom: 14px;
}

.features-box {
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 28px;
    box-shadow: var(--shadow);
    overflow: hidden;
}

.feature-row {
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 18px 22px;
    border-bottom: 1px solid var(--line);
}

.feature-row:last-child {
    border-bottom: 0;
}

.check {
    width: 34px;
    height: 34px;
    display: grid;
    place-items: center;
    border-radius: 50%;
    background: rgba(15, 118, 110, 0.12);
    color: var(--accent);
    font-weight: 800;
    flex: 0 0 34px;
}

.partner-badge {
    display: inline-block;
    margin-bottom: 12px;
    padding: 7px 12px;
    border-radius: 999px;
    background: rgba(29, 78, 216, 0.10);
    color: var(--primary);
    font-weight: 700;
    font-size: 0.88rem;
}

.contact-grid {
    display: grid;
    grid-template-columns: 0.9fr 1.1fr;
    gap: 28px;
    align-items: start;
}

.contact-form {
    padding: 26px;
}

.contact-form label {
    display: block;
    margin-bottom: 8px;
    font-weight: 700;
}

.contact-form input,
.contact-form textarea {
    width: 100%;
    padding: 14px 16px;
    margin-bottom: 16px;
    border: 1px solid var(--line);
    border-radius: 14px;
    font: inherit;
    color: var(--text);
    background: #fff;
}

.contact-form textarea {
    resize: vertical;
    min-height: 140px;
}

.form-alert {
    margin-bottom: 16px;
    padding: 14px 16px;
    border-radius: 14px;
    background: rgba(29, 78, 216, 0.08);
    color: var(--primary-dark);
    font-weight: 700;
}

.site-footer {
    padding: 28px 0;
    background: #0f172a;
    color: rgba(255, 255, 255, 0.88);
}

.footer-wrap {
    display: flex;
    justify-content: space-between;
    gap: 20px;
    flex-wrap: wrap;
}

@media (max-width: 1024px) {
    .hero-grid,
    .contact-grid,
    .about-grid,
    .card-grid,
    .audience-grid,
    .partners-grid {
        grid-template-columns: 1fr 1fr;
    }

    .hero-points {
        grid-template-columns: 1fr;
    }

    .main-nav {
        display: none;
    }
}

@media (max-width: 640px) {
    .hero-grid,
    .contact-grid,
    .about-grid,
    .card-grid,
    .audience-grid,
    .partners-grid {
        grid-template-columns: 1fr;
    }

    .hero {
        padding-top: 72px;
    }

    .nav-wrap {
        min-height: 68px;
    }

    .brand-text {
        font-size: 0.92rem;
    }

    .nav-cta {
        display: none;
    }
}
"""
