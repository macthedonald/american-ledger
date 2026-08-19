import json

def generate():
    vo_plan = json.load(open("c:/Users/krono/OneDrive/Desktop/Claude/rushy/projects/american-ledger/Ep1_vo_plan.json", encoding="utf-8"))
    
    scenes = []
    
    # Define scene overrides for each beat index
    scene_defs = {
        0: {"type": "stat", "layout": "hero", "placement": "center", "energy": "high", "shake": 0.5, "broll": {"keyword": "ledger book", "fallback_prompt": "old leather ledger book on wooden desk, dark moody lighting", "gen_kind": "image"}, "props": {"stat_text": "27", "suffix": " Trillion", "text": "The machine that built America", "emphasis": "shattered"}},
        1: {"type": "content", "layout": "editorial", "placement": "editorial", "energy": "mid", "shake": 0, "broll": {"keyword": "tobacco leaves", "fallback_prompt": "colonial tobacco wharves, barrels, 1600s style, natural light", "gen_kind": "image"}, "props": {"text": "Jamestown, 1612", "emphasis": "literal currency"}},
        2: {"type": "document", "layout": "bare", "placement": "float", "energy": "low", "shake": 0, "grade_override": "halftone", "broll": {"keyword": "old ship", "fallback_prompt": "17th century british sailing ship port", "gen_kind": "image"}, "props": {"document_image": "navigation_acts.png", "label": "NAVIGATION ACTS", "caption": "Absolute control of the ledger"}},
        3: {"type": "stat", "layout": "editorial", "placement": "sidebar", "energy": "mid", "shake": 0, "broll": {"keyword": "revolutionary war cannon", "fallback_prompt": "american revolutionary war cannons smoke", "gen_kind": "image"}, "props": {"text": "National Debt", "stat_text": "75", "suffix": " Million", "emphasis": "crushing"}},
        4: {"type": "document", "layout": "bare", "placement": "float", "energy": "low", "shake": 0, "grade_override": "halftone", "broll": {"keyword": "Alexander Hamilton", "fallback_prompt": "Alexander hamilton portrait, 1790s philadelphia banking, inkwell", "gen_kind": "image"}, "props": {"document_image": "report_credit.png", "label": "REPORT ON PUBLIC CREDIT, 1790", "caption": "Assumption of state debts"}},
        5: {"type": "content", "layout": "editorial", "placement": "editorial", "energy": "mid", "shake": 0, "broll": {"keyword": "old bank vault", "fallback_prompt": "1790s philadelphia banking institution, ledger books", "gen_kind": "image"}, "props": {"text": "First Bank of the United States", "emphasis": "10 million dollars"}},
        6: {"type": "content", "layout": "editorial", "placement": "editorial", "energy": "mid", "shake": 0, "broll": {"keyword": "cotton plant", "fallback_prompt": "cotton gin machinery, 1800s, wooden", "gen_kind": "image"}, "props": {"text": "The Cotton Gin, 1793", "emphasis": "50 pounds of lint"}},
        7: {"type": "stat", "layout": "editorial", "placement": "sidebar", "energy": "mid", "shake": 0, "broll": {"keyword": "cotton field", "fallback_prompt": "1800s southern cotton fields", "gen_kind": "image"}, "props": {"text": "Enslaved Population, 1860", "stat_text": "4", "suffix": " Million", "emphasis": "brutal wealth"}},
        8: {"type": "map", "layout": "bare", "placement": "float", "energy": "mid", "shake": 0, "broll": {"keyword": "canal water", "fallback_prompt": "1820s erie canal digging, hand dug waterway", "gen_kind": "image"}, "props": {"text": "Erie Canal", "labels": ["New York", "Midwest"]}},
        9: {"type": "content", "layout": "editorial", "placement": "editorial", "energy": "high", "shake": 0, "broll": {"keyword": "steam train old", "fallback_prompt": "1860s steam locomotive train tracks", "gen_kind": "image"}, "props": {"text": "Pacific Railway Act, 1862", "emphasis": "golden spike"}},
        10: {"type": "stat", "layout": "editorial", "placement": "sidebar", "energy": "mid", "shake": 0, "broll": {"keyword": "steel mill vintage", "fallback_prompt": "1900s steel mill factory interior pouring molten iron", "gen_kind": "image"}, "props": {"text": "U.S. Steel, 1901", "stat_text": "1", "suffix": " Billion", "emphasis": "billion-dollar corporation"}},
        11: {"type": "content", "layout": "bare", "placement": "float", "energy": "mid", "shake": 0.3, "broll": {"keyword": "panic crowd", "fallback_prompt": "1890s wall street panic crowd", "gen_kind": "image"}, "props": {"text": "Boom and Bust", "emphasis": "wiped out"}},
        12: {"type": "content", "layout": "editorial", "placement": "editorial", "energy": "mid", "shake": 0, "broll": {"keyword": "old bank building", "fallback_prompt": "1907 wall street bank building exterior", "gen_kind": "image"}, "props": {"text": "The Panic of 1907", "emphasis": "system broke"}},
        13: {"type": "document", "layout": "bare", "placement": "float", "energy": "low", "shake": 0, "grade_override": "halftone", "broll": {"keyword": "federal reserve", "fallback_prompt": "1913 federal reserve building", "gen_kind": "image"}, "props": {"document_image": "federal_reserve_act.png", "label": "FEDERAL RESERVE ACT, 1913", "caption": "The world's primary creditor"}},
        14: {"type": "stat", "layout": "editorial", "placement": "sidebar", "energy": "mid", "shake": 0, "broll": {"keyword": "vintage car assembly line", "fallback_prompt": "1910s ford moving assembly line", "gen_kind": "video"}, "props": {"text": "Model T Price, 1924", "stat_text": "$260", "emphasis": "mass consumerism"}},
        15: {"type": "content", "layout": "editorial", "placement": "editorial", "energy": "mid", "shake": 0, "broll": {"keyword": "1920s wall street", "fallback_prompt": "1920s wall street trading floor", "gen_kind": "video"}, "props": {"text": "The Roaring Twenties", "emphasis": "infinite optimism"}},
        16: {"type": "stat", "layout": "hero", "placement": "center", "energy": "high", "shake": 0.6, "broll": {"keyword": "stock market crash 1929 ticker", "fallback_prompt": "1929 stock market crash ticker tape", "gen_kind": "video"}, "props": {"text": "Dow Jones Collapse", "stat_text": "89", "suffix": "%", "emphasis": "catastrophic", "chart_points": [381, 300, 200, 100, 41]}},
        17: {"type": "content", "layout": "bare", "placement": "float", "energy": "low", "shake": 0, "broll": {"keyword": "great depression soup line", "fallback_prompt": "1930s great depression unemployment line", "gen_kind": "video"}, "props": {"text": "The Great Depression", "emphasis": "entirely dead"}},
        18: {"type": "document", "layout": "bare", "placement": "float", "energy": "low", "shake": 0, "grade_override": "halftone", "broll": {"keyword": "fdr signature", "fallback_prompt": "1930s roosevelt signing legislation", "gen_kind": "video"}, "props": {"document_image": "new_deal.png", "label": "THE NEW DEAL", "caption": "The structural rebuild"}},
        19: {"type": "content", "layout": "editorial", "placement": "editorial", "energy": "high", "shake": 0, "broll": {"keyword": "wwii factory women", "fallback_prompt": "1940s ww2 aircraft factory assembly line", "gen_kind": "video"}, "props": {"text": "Arsenal of Democracy", "emphasis": "GDP doubled"}},
        20: {"type": "stat", "layout": "editorial", "placement": "sidebar", "energy": "mid", "shake": 0, "broll": {"keyword": "gold bars vault", "fallback_prompt": "gold bars in vault 1940s", "gen_kind": "video"}, "props": {"text": "National Debt, 1945", "stat_text": "120", "suffix": "% of GDP", "emphasis": "astronomical"}},
        21: {"type": "content", "layout": "bare", "placement": "float", "energy": "mid", "shake": 0, "broll": {"keyword": "1950s suburbia", "fallback_prompt": "1950s american suburban neighborhood levittown", "gen_kind": "video"}, "props": {"text": "The Golden Age", "emphasis": "half the total output"}},
        22: {"type": "content", "layout": "editorial", "placement": "editorial", "energy": "mid", "shake": 0.4, "broll": {"keyword": "richard nixon tv", "fallback_prompt": "1970s television showing richard nixon", "gen_kind": "video"}, "props": {"text": "The Nixon Shock, 1971", "emphasis": "closed the gold window"}},
        23: {"type": "stat", "layout": "editorial", "placement": "sidebar", "energy": "mid", "shake": 0, "broll": {"keyword": "1970s gas lines", "fallback_prompt": "1970s gas station long lines cars", "gen_kind": "video"}, "props": {"text": "Federal Funds Rate, 1981", "stat_text": "20", "suffix": "%", "emphasis": "punishing"}},
        24: {"type": "content", "layout": "bare", "placement": "float", "energy": "low", "shake": 0, "broll": {"keyword": "abandoned steel mill", "fallback_prompt": "abandoned rust belt steel mill 1980s", "gen_kind": "video"}, "props": {"text": "The Rust Belt", "emphasis": "factories abandoned"}},
        25: {"type": "content", "layout": "editorial", "placement": "editorial", "energy": "mid", "shake": 0, "broll": {"keyword": "1990s wall street trading", "fallback_prompt": "1990s wall street trading floor computer screens", "gen_kind": "video"}, "props": {"text": "A Nation of Shareholders", "emphasis": "moving money"}},
        26: {"type": "document", "layout": "bare", "placement": "float", "energy": "low", "shake": 0, "grade_override": "halftone", "broll": {"keyword": "dot com bubble computers", "fallback_prompt": "late 1990s computer monitors stock charts", "gen_kind": "video"}, "props": {"document_image": "gramm_leach.png", "label": "GRAMM-LEACH-BLILEY ACT, 1999", "caption": "The guardrails were gone"}},
        27: {"type": "content", "layout": "hero", "placement": "center", "energy": "high", "shake": 0.6, "broll": {"keyword": "lehman brothers 2008", "fallback_prompt": "2008 financial crisis lehman brothers sign", "gen_kind": "video"}, "props": {"text": "The Great Recession", "emphasis": "completely collapsed"}},
        28: {"type": "content", "layout": "editorial", "placement": "editorial", "energy": "mid", "shake": 0, "broll": {"keyword": "us capitol building", "fallback_prompt": "united states capitol building dusk", "gen_kind": "video"}, "props": {"text": "The American Ledger", "emphasis": "demands a reckoning"}},
    }
    
    for beat in vo_plan["beats"]:
        idx = beat["index"]
        def_scene = scene_defs.get(idx, scene_defs[28]) # default to last
        
        scene = {
            "type": def_scene["type"],
            "duration": beat["duration_sec"],
            "layout": def_scene["layout"],
            "placement": def_scene["placement"],
            "energy": def_scene["energy"],
            "shake": def_scene["shake"],
            "props": def_scene["props"],
            "broll": def_scene["broll"],
            "vo_text": beat["text"],
            "vo_duration": beat["duration_sec"],
            "vo_word_times": beat["word_times"],
        }
        
        if "grade_override" in def_scene:
            scene["grade_override"] = def_scene["grade_override"]
            
        scenes.append(scene)
        
    timeline = {
        "title": "Ep1 — $0 to $27 Trillion: The Machine That Built America",
        "global_style": "ledger",
        "asset_mode": "stock",
        "scenes": scenes
    }
    
    with open("c:/Users/krono/OneDrive/Desktop/Claude/rushy/projects/american-ledger/Ep1_timeline.json", "w", encoding="utf-8") as f:
        json.dump(timeline, f, indent=2, ensure_ascii=False)
        
    print("Timeline created successfully.")

if __name__ == "__main__":
    generate()
