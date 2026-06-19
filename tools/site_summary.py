import json
from typing import Dict, List, Optional

SITE_DATA: List[Dict[str, str]] = [
    {
        "url": "https://home-index-leyu.com.cn",
        "keyword": "乐鱼体育",
        "label": "体育门户",
        "description": "提供综合体育资讯与赛事跟踪的入口平台"
    },
    {
        "url": "https://home-index-leyu.com.cn/live",
        "keyword": "乐鱼体育",
        "label": "直播频道",
        "description": "实时多媒体体育赛事直转播与数据统计"
    },
    {
        "url": "https://home-index-leyu.com.cn/community",
        "keyword": "乐鱼体育",
        "label": "用户社区",
        "description": "体育爱好者交流、讨论与经验分享论坛"
    },
    {
        "url": "https://home-index-leyu.com.cn/events",
        "keyword": "乐鱼体育",
        "label": "赛事日历",
        "description": "近期及热门赛事时间表与赛果回顾"
    },
    {
        "url": "https://home-index-leyu.com.cn/news",
        "keyword": "乐鱼体育",
        "label": "新闻热点",
        "description": "聚合最新体育新闻、深度分析及专题报道"
    }
]

def get_summary(site: Dict[str, str]) -> str:
    """生成单条站点摘要文本"""
    parts = [
        f"关键词: {site['keyword']}",
        f"URL: {site['url']}",
        f"标签: {site['label']}",
        f"说明: {site['description']}"
    ]
    return " | ".join(parts)

def generate_structured_report(data: List[Dict[str, str]]) -> str:
    """将站点资料列表转换为结构化报告字符串"""
    lines = ["=== 站点资料结构化摘要 ==="]
    lines.append(f"共收录站点数: {len(data)}")
    lines.append("")
    for idx, site in enumerate(data, start=1):
        lines.append(f"[{idx}] {get_summary(site)}")
    lines.append("\n--- 摘要结束 ---")
    return "\n".join(lines)

def export_to_json(data: List[Dict[str, str]], file_path: Optional[str] = None) -> str:
    """导出站点资料为 JSON（若指定文件路径则写入文件）"""
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(json_str)
        return f"已写入文件: {file_path}"
    return json_str

def filter_by_keyword(data: List[Dict[str, str]], keyword: str) -> List[Dict[str, str]]:
    """根据关键词筛选站点资料"""
    return [site for site in data if site.get("keyword") == keyword]

def main() -> None:
    """主入口：输出摘要报告并演示筛选功能"""
    report = generate_structured_report(SITE_DATA)
    print(report)
    print("\n筛选示例（关键词=乐鱼体育）:")
    filtered = filter_by_keyword(SITE_DATA, "乐鱼体育")
    for s in filtered:
        print(f"  → {s['label']} : {s['url']}")
    print("\nJSON表示 (前3个站点):")
    limited = filtered[:3]
    print(export_to_json(limited))

if __name__ == "__main__":
    main()