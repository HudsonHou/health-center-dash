// assets/js/1-custom.js
function initializeFinisher() {
    const container = document.querySelector('.finisher-header');
    if (!container) {
        // 如果容器不存在，延迟 100ms 后重试
        setTimeout(initializeFinisher, 100);
        return;
    }

    new FinisherHeader({
        count: 90,
        size: { min: 1, max: 20, pulse: 0 },
        speed: { 
            x: { min: 0, max: 0.4 },
            y: { min: 0, max: 0.1 }
        },
        colors: {
            background: "#2558a2",
            particles: ["#ffffff", "#87ddfe", "#accaff", "#1bffc2", "#f88aff"]
        },
        blending: "screen",
        opacity: { center: 0, edge: 0.4 },
        skew: -2,
        shapes: ["c", "s", "t"]
    });
}

// 首次初始化尝试
document.addEventListener('DOMContentLoaded', initializeFinisher);

// Dash 动态加载后重新初始化（针对单页面应用）
document.addEventListener('dash_mounted', initializeFinisher);