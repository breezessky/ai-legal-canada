#!/bin/bash
# ============================================================================
# AI Legal Assistant — Canadian Edition
# Claude Code Skills Installer
# 14 Skills · 5 Agents · PDF Reports · Built for Canadian Law
#
# Frameworks covered:
#   PIPEDA · CASL · Law 25 (Quebec) · PIPA (BC/AB) · Canada Labour Code
#   AODA · Competition Act · Provincial ESAs · Consumer Protection Acts
# ============================================================================
set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m'

echo ""
echo -e "${BLUE}╔══════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║                                                                  ║${NC}"
echo -e "${BLUE}║${NC}   ${WHITE}🍁 AI Legal Assistant — Canadian Edition${NC}                      ${BLUE}║${NC}"
echo -e "${BLUE}║${NC}   ${GREEN}14 Skills · 5 Agents · PDF Reports · Built for Canadian Law${NC}   ${BLUE}║${NC}"
echo -e "${BLUE}║                                                                  ║${NC}"
echo -e "${BLUE}║${NC}   ${CYAN}PIPEDA · CASL · Law 25 · PIPA · Canada Labour Code${NC}             ${BLUE}║${NC}"
echo -e "${BLUE}║${NC}   ${CYAN}AODA · Competition Act · Provincial ESAs · CPA${NC}                 ${BLUE}║${NC}"
echo -e "${BLUE}║                                                                  ║${NC}"
echo -e "${BLUE}╚══════════════════════════════════════════════════════════════════╝${NC}"
echo ""

# ---------------------------------------------------------------------------
# Detect script directory (handle both local and curl | bash)
# ---------------------------------------------------------------------------
GITHUB_REPO="breezessky/ai-legal-canada"
TEMP_DIR=""

if [ -n "${BASH_SOURCE[0]}" ] && [ "${BASH_SOURCE[0]}" != "bash" ]; then
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    if [ -f "$SCRIPT_DIR/install.sh" ] && [ -d "$SCRIPT_DIR/skills" ]; then
        SOURCE_DIR="$SCRIPT_DIR"
        echo -e "${GREEN}Installing from local directory:${NC} $SOURCE_DIR"
    else
        SCRIPT_DIR=""
    fi
fi

if [ -z "${SCRIPT_DIR:-}" ] || [ ! -d "${SOURCE_DIR:-}" ]; then
    echo -e "${YELLOW}Cloning from GitHub...${NC}"
    TEMP_DIR=$(mktemp -d)
    if command -v git &>/dev/null; then
        git clone --depth 1 "https://github.com/$GITHUB_REPO.git" "$TEMP_DIR/repo" 2>/dev/null
        SOURCE_DIR="$TEMP_DIR/repo"
    else
        echo -e "${RED}Error: git is required for remote installation.${NC}"
        echo "Install git or run install.sh from a local clone."
        exit 1
    fi
    echo -e "${GREEN}Cloned successfully.${NC}"
fi

# ---------------------------------------------------------------------------
# Target directories
# ---------------------------------------------------------------------------
SKILLS_DIR="$HOME/.claude/skills"
AGENTS_DIR="$HOME/.claude/agents"

# ---------------------------------------------------------------------------
# Check for Claude Code
# ---------------------------------------------------------------------------
echo -e "${BLUE}Checking prerequisites...${NC}"
if command -v claude &>/dev/null; then
    echo -e "  ${GREEN}✓${NC} Claude Code found"
else
    echo -e "  ${YELLOW}⚠${NC} Claude Code CLI not found (skills will still be installed)"
fi

# ---------------------------------------------------------------------------
# Create directories
# ---------------------------------------------------------------------------
echo -e "${BLUE}Creating directories...${NC}"
mkdir -p "$SKILLS_DIR/legal/scripts"
mkdir -p "$SKILLS_DIR/legal/templates"
echo -e "  ${GREEN}✓${NC} Skills directory: $SKILLS_DIR"

mkdir -p "$AGENTS_DIR"
echo -e "  ${GREEN}✓${NC} Agents directory: $AGENTS_DIR"

# ---------------------------------------------------------------------------
# Install main skill orchestrator
# ---------------------------------------------------------------------------
echo ""
echo -e "${BLUE}Installing skills...${NC}"

INSTALL_COUNT=0

if [ -f "$SOURCE_DIR/legal/SKILL.md" ]; then
    cp "$SOURCE_DIR/legal/SKILL.md" "$SKILLS_DIR/legal/SKILL.md"
    echo -e "  ${GREEN}✓${NC} legal (Canadian orchestrator)"
    INSTALL_COUNT=$((INSTALL_COUNT + 1))
fi

# ---------------------------------------------------------------------------
# Install 13 sub-skills
# ---------------------------------------------------------------------------
SKILLS=(
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
    if [ -f "$SOURCE_DIR/skills/$skill/SKILL.md" ]; then
        mkdir -p "$SKILLS_DIR/$skill"
        cp "$SOURCE_DIR/skills/$skill/SKILL.md" "$SKILLS_DIR/$skill/SKILL.md"
        echo -e "  ${GREEN}✓${NC} $skill"
        INSTALL_COUNT=$((INSTALL_COUNT + 1))
    else
        echo -e "  ${YELLOW}⚠${NC} $skill (not found in source)"
    fi
done

# ---------------------------------------------------------------------------
# Install 5 agents
# ---------------------------------------------------------------------------
echo ""
echo -e "${BLUE}Installing agents...${NC}"

AGENT_COUNT=0
AGENTS=(
    legal-clauses
    legal-risks
    legal-compliance
    legal-terms
    legal-recommendations
)

for agent in "${AGENTS[@]}"; do
    if [ -f "$SOURCE_DIR/agents/$agent.md" ]; then
        cp "$SOURCE_DIR/agents/$agent.md" "$AGENTS_DIR/$agent.md"
        echo -e "  ${GREEN}✓${NC} $agent"
        AGENT_COUNT=$((AGENT_COUNT + 1))
    else
        echo -e "  ${YELLOW}⚠${NC} $agent (not found in source)"
    fi
done

# ---------------------------------------------------------------------------
# Install Python scripts
# ---------------------------------------------------------------------------
echo ""
echo -e "${BLUE}Installing PDF generator...${NC}"

SCRIPT_COUNT=0
for script in "$SOURCE_DIR"/scripts/*.py; do
    if [ -f "$script" ]; then
        cp "$script" "$SKILLS_DIR/legal/scripts/"
        echo -e "  ${GREEN}✓${NC} $(basename "$script")"
        SCRIPT_COUNT=$((SCRIPT_COUNT + 1))
    fi
done

# ---------------------------------------------------------------------------
# Install templates
# ---------------------------------------------------------------------------
echo ""
echo -e "${BLUE}Installing templates...${NC}"

TEMPLATE_COUNT=0
for template in "$SOURCE_DIR"/templates/*.md; do
    if [ -f "$template" ]; then
        cp "$template" "$SKILLS_DIR/legal/templates/"
        echo -e "  ${GREEN}✓${NC} $(basename "$template")"
        TEMPLATE_COUNT=$((TEMPLATE_COUNT + 1))
    fi
done

# ---------------------------------------------------------------------------
# Check Python dependencies
# ---------------------------------------------------------------------------
echo ""
echo -e "${BLUE}Checking Python environment...${NC}"

if command -v python3 &>/dev/null; then
    echo -e "  ${GREEN}✓${NC} Python 3 found: $(python3 --version 2>&1)"
else
    echo -e "  ${RED}✗${NC} Python 3 not found — required for PDF reports"
fi

if python3 -c "import reportlab" 2>/dev/null; then
    echo -e "  ${GREEN}✓${NC} reportlab installed"
else
    echo -e "  ${YELLOW}⚠${NC} reportlab not installed (needed for PDF reports)"
    echo -e "      Install with: ${CYAN}pip3 install reportlab${NC}"
fi

# ---------------------------------------------------------------------------
# Cleanup temp dir if used
# ---------------------------------------------------------------------------
if [ -n "$TEMP_DIR" ] && [ -d "$TEMP_DIR" ]; then
    rm -rf "$TEMP_DIR"
    echo -e "  ${GREEN}✓${NC} Cleaned up temporary files"
fi

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
echo ""
echo -e "${GREEN}╔══════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║  🍁 Installation Complete — Canadian Edition                     ║${NC}"
echo -e "${GREEN}╚══════════════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "  ${CYAN}Skills:${NC}    $INSTALL_COUNT installed  →  $SKILLS_DIR"
echo -e "  ${CYAN}Agents:${NC}    $AGENT_COUNT installed  →  $AGENTS_DIR"
echo -e "  ${CYAN}Scripts:${NC}   $SCRIPT_COUNT installed  →  $SKILLS_DIR/legal/scripts"
echo -e "  ${CYAN}Templates:${NC} $TEMPLATE_COUNT installed  →  $SKILLS_DIR/legal/templates"
echo ""

# ---------------------------------------------------------------------------
# Command reference — Canadian Edition
# ---------------------------------------------------------------------------
echo -e "${BLUE}🍁 Canadian Edition — Command Reference:${NC}"
echo ""
echo -e "  ${CYAN}/legal review <file>${NC}            Full review — 5 agents, Canadian law"
echo -e "  ${CYAN}/legal risks <file>${NC}             Risk analysis (CAD exposure)"
echo -e "  ${CYAN}/legal compare <f1> <f2>${NC}        Side-by-side comparison"
echo -e "  ${CYAN}/legal plain <file>${NC}             Plain English / French translation"
echo -e "  ${CYAN}/legal negotiate <file>${NC}         Counter-proposals (Canadian law)"
echo -e "  ${CYAN}/legal missing <file>${NC}           Missing Canadian-law protections"
echo -e "  ${CYAN}/legal nda <description>${NC}        NDA — common law or Quebec civil law"
echo -e "  ${CYAN}/legal terms <url>${NC}              Terms of service — CASL compliant"
echo -e "  ${CYAN}/legal privacy <url>${NC}            Privacy policy — PIPEDA / Law 25"
echo -e "  ${CYAN}/legal agreement <type>${NC}         Business agreements — Canadian law"
echo -e "  ${CYAN}/legal freelancer <file>${NC}        Contractor review — CRA classification"
echo -e "  ${CYAN}/legal compliance <url>${NC}         PIPEDA · CASL · AODA · Law 25 audit"
echo -e "  ${CYAN}/legal casl <description>${NC}       🆕 CASL email/marketing compliance"
echo -e "  ${CYAN}/legal report-pdf${NC}               Professional PDF report"
echo ""
echo -e "  ${YELLOW}Tip:${NC} Start with ${CYAN}/legal review <file>${NC} for a full Canadian law analysis!"
echo -e "  ${YELLOW}New:${NC} ${CYAN}/legal casl${NC} is unique to this Canadian edition — no US/EU equivalent!"
echo ""
echo -e "${BLUE}Covered Frameworks:${NC}"
echo -e "  PIPEDA · Bill C-27/CPPA · Law 25 (Quebec) · BC PIPA · AB PIPA"
echo -e "  CASL · AODA · Competition Act · Canada Labour Code"
echo -e "  Provincial ESAs · Consumer Protection Acts · Civil Code of Quebec"
echo ""
