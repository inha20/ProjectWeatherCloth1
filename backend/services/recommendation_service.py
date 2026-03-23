from typing import Dict, Any, List
from ..models import RecommendationResult

class RecommendationService:
    # Warmth Score (CLO equivalent) for each item category
    # Values: 1.0 = very warm, 0.1 = very cool
    ITEMS = {
        "outer": [
            {"name": "롱패딩", "score": 1.0, "min_temp": -20, "max_temp": 5},
            {"name": "숏패딩", "score": 0.8, "min_temp": -5, "max_temp": 10},
            {"name": "코트", "score": 0.7, "min_temp": 0, "max_temp": 12},
            {"name": "가디건", "score": 0.3, "min_temp": 12, "max_temp": 20},
            {"name": "바람막이", "score": 0.2, "min_temp": 15, "max_temp": 23},
        ],
        "top": [
            {"name": "니트", "score": 0.5, "min_temp": -20, "max_temp": 15},
            {"name": "맨투맨", "score": 0.4, "min_temp": 5, "max_temp": 20},
            {"name": "긴팔티", "score": 0.3, "min_temp": 15, "max_temp": 25},
            {"name": "반팔티", "score": 0.1, "min_temp": 23, "max_temp": 40},
        ],
        "bottom": [
            {"name": "기모바지", "score": 0.5, "min_temp": -20, "max_temp": 10},
            {"name": "청바지", "score": 0.3, "min_temp": 5, "max_temp": 25},
            {"name": "반바지", "score": 0.1, "min_temp": 25, "max_temp": 40},
        ]
    }

    @staticmethod
    def get_recommendation(temp: float, humidity: int, rain: int, sensitivity: int = 3) -> RecommendationResult:
        # 1. Calculate target warmth score (Required CLO)
        # Base: 30C -> 0.2 (T-shirt), 0C -> 1.5 (Heavy)
        target_score = (30 - temp) * 0.05 + 0.1
        
        # 2. Adjust for sensitivity (1~5, 3 is normal)
        sensitivity_offset = (sensitivity - 3) * 0.1
        target_score += sensitivity_offset
        
        # 3. Adjust for humidity & rain
        if humidity > 80: target_score += 0.05
        if rain > 50: target_score += 0.1
        
        # 4. Select items (Greedy selection for simplicity)
        recommended = {"outer": None, "top": "반팔티", "bottom": "청바지", "shoes": "운동화", "accessories": []}
        current_score = 0.0
        
        # Pick top
        for item in sorted(RecommendationService.ITEMS["top"], key=lambda x: abs(x["score"] - (target_score * 0.4)), reverse=True):
            if item["min_temp"] <= temp <= item["max_temp"]:
                recommended["top"] = item["name"]
                current_score += item["score"]
                break
        
        # Pick bottom
        for item in sorted(RecommendationService.ITEMS["bottom"], key=lambda x: abs(x["score"] - (target_score * 0.3)), reverse=True):
            if item["min_temp"] <= temp <= item["max_temp"]:
                recommended["bottom"] = item["name"]
                current_score += item["score"]
                break
                
        # Pick outer if needed
        if target_score - current_score > 0.15:
            for item in sorted(RecommendationService.ITEMS["outer"], key=lambda x: abs(x["score"] - (target_score - current_score)), reverse=True):
                if item["min_temp"] <= temp <= item["max_temp"]:
                    recommended["outer"] = item["name"]
                    current_score += item["score"]
                    break
        
        # Accessories
        tips = []
        if rain > 30: 
            recommended["accessories"].append("우산")
            tips.append("☔ 비 소식이 있습니다. 우산을 챙기세요.")
        if temp < 5:
            recommended["accessories"].append("목도리")
            tips.append("🧣 기온이 낮습니다. 목을 따뜻하게 보호하세요.")
            
        return RecommendationResult(
            outer=recommended["outer"],
            top=recommended["top"],
            bottom=recommended["bottom"],
            shoes=recommended["shoes"],
            accessories=recommended["accessories"],
            warmth_score=round(current_score, 2),
            tips=tips
        )
