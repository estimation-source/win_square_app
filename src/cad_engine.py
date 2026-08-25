import io
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_window_cad(width: int, height: int, win_type: str) -> io.BytesIO:
    """Generates a dynamic 2D technical window layout drawing."""
    fig, ax = plt.subplots(figsize=(3.5, 3.2))
    
    padding = max(width, height) * 0.15
    ax.set_xlim(-padding, width + padding)
    ax.set_ylim(-padding, height + padding)
    ax.set_aspect('equal')
    ax.axis('off')

    # Outer Frame Boundary
    outer_frame = patches.Rectangle((0, 0), width, height, linewidth=2, edgecolor='#1e293b', facecolor='#e0f2fe')
    ax.add_patch(outer_frame)
    
    # Inner Glass Sash Frame
    frame_thick = min(width, height) * 0.05
    inner_glass = patches.Rectangle(
        (frame_thick, frame_thick), 
        width - 2*frame_thick, 
        height - 2*frame_thick, 
        linewidth=1, 
        edgecolor='#0284c7', 
        facecolor='#bae6fd', 
        alpha=0.7
    )
    ax.add_patch(inner_glass)

    # Internal Mullion / Sliding Lines
    if "Sliding" in win_type or width > 1500:
        mid_x = width / 2
        ax.plot([mid_x, mid_x], [frame_thick, height - frame_thick], color='#0284c7', linewidth=1.5)
        ax.annotate('', xy=(mid_x - frame_thick, height/2), xytext=(frame_thick*2, height/2),
                    arrowprops=dict(arrowstyle="->", color="#0369a1", lw=1))
        ax.annotate('', xy=(mid_x + frame_thick, height/2), xytext=(width - frame_thick*2, height/2),
                    arrowprops=dict(arrowstyle="->", color="#0369a1", lw=1))

    # Center Glass Tag Icon
    ax.text(width/2, height/2, "1", color='#0369a1', weight='bold', fontsize=9,
            bbox=dict(boxstyle="circle,pad=0.3", fc="white", ec="#0284c7", lw=1),
            ha='center', va='center')

    # Scale Dimensions Text Lines
    ax.text(-padding*0.4, height/2, f"{height}", va='center', ha='right', rotation='vertical', fontsize=9, weight='bold', color='#334155')
    ax.text(width/2, -padding*0.4, f"{width}", va='top', ha='center', fontsize=9, weight='bold', color='#334155')

    # Extension Dimension Indicator Lines
    ax.plot([-padding*0.2, 0], [0, 0], color='#94a3b8', lw=0.8)
    ax.plot([-padding*0.2, 0], [height, height], color='#94a3b8', lw=0.8)
    ax.plot([-padding*0.1, -padding*0.1], [0, height], color='#94a3b8', lw=0.8)

    ax.plot([0, 0], [-padding*0.2, 0], color='#94a3b8', lw=0.8)
    ax.plot([width, width], [-padding*0.2, 0], color='#94a3b8', lw=0.8)
    ax.plot([0, width], [-padding*0.1, -padding*0.1], color='#94a3b8', lw=0.8)

    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', dpi=180, transparent=True)
    plt.close(fig)
    buf.seek(0)
    return buf
