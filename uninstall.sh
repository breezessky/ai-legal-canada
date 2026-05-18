#!/bin/bash
# ============================================================================
# AI Legal Assistant — Canadian Edition
# Uninstaller
# ============================================================================
set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

SKILLS_DIR="$HOME/.claude/skills"
AGENTS_DIR="$HOME/.claude/agents"

echo ""
echo -e "${YELLOW}╔══════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${YELLOW}║  🍁 AI Legal Assistant — Canadian Edition: Uninstaller           ║${NC}"
echo -e "${YELLOW}╚══════════════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${RED}This will remove all AI Legal Assistant (Canadian Edition) files.${NC}"
echo -n "Are you sure? (y/N): "
read -r confirm
if [[ "$confirm" != "y" && "$confirm" != "Y" ]]; then
    echo -e "${GREEN}Uninstall cancelled.${NC}"
    exit 0
fi

echo ""
echo -e "${BLUE}Removing skills...${NC}"

SKILLS=(
    legal
    legal-review
    legal-risks
    legal-compare
    legal-plain
    legal-negotiate
    legal-missing
    legal-nda
    legal-terms
    legal-privacy
    legal-agreement
    legal-compliance
    legal-freelancer
    legal-casl
    legal-report-pdf
)

for skill in "${SKILLS[@]}"; do
    if [ -d "$SKILLS_DIR/$skill" ]; then
        rm -rf "$SKILLS_DIR/$skill"
        echo -e "  ${GREEN}✓${NC} Removed: $skill"
    else
        echo -e "  ${YELLOW}—${NC} Not found: $skill (skipped)"
    fi
done

echo ""
echo -e "${BLUE}Removing agents...${NC}"

AGENTS=(
    legal-clauses
    legal-risks
    legal-compliance
    legal-terms
    legal-recommendations
)

for agent in "${AGENTS[@]}"; do
    if [ -f "$AGENTS_DIR/$agent.md" ]; then
        rm -f "$AGENTS_DIR/$agent.md"
        echo -e "  ${GREEN}✓${NC} Removed: $agent"
    else
        echo -e "  ${YELLOW}—${NC} Not found: $agent (skipped)"
    fi
done

echo ""
echo -e "${GREEN}╔══════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║  Uninstall complete.                                             ║${NC}"
echo -e "${GREEN}╚══════════════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "  Reinstall anytime:"
echo -e "  ${CYAN}curl -fsSL https://raw.githubusercontent.com/jonlin/ai-legal-canada/main/install.sh | bash${NC}"
echo ""
