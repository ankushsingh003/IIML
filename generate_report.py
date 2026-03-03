from fpdf import FPDF 
import os 
import pandas as pd 

class InsightifyReport (FPDF ):
    def header (self ):

        self .set_fill_color (63 ,81 ,181 )
        self .rect (0 ,0 ,210 ,15 ,'F')

        self .set_y (5 )
        self .set_font ('Arial','B',12 )
        self .set_text_color (255 ,255 ,255 )
        self .cell (0 ,5 ,'INSIGHTIFY | BI REPORT',0 ,1 ,'L')
        self .ln (10 )

    def footer (self ):
        self .set_y (-15 )
        self .set_font ('Arial','I',8 )
        self .set_text_color (128 ,128 ,128 )
        self .cell (0 ,10 ,f'Insightify Restaurant Analysis - Page {self .page_no ()}',0 ,0 ,'C')

    def chapter_title (self ,title ):
        self .set_font ('Arial','B',14 )
        self .set_text_color (63 ,81 ,181 )
        self .cell (0 ,10 ,title ,0 ,1 ,'L')
        self .line (self .get_x (),self .get_y (),self .get_x ()+190 ,self .get_y ())
        self .ln (5 )

    def add_insight_text (self ,text ):
        self .set_font ('Arial','',11 )
        self .set_text_color (50 ,50 ,50 )
        self .multi_cell (0 ,8 ,text )
        self .ln (3 )

def create_enhanced_pdf (stats ,visuals_dir ,output_pdf ):
    pdf =InsightifyReport ()
    pdf .set_auto_page_break (auto =True ,margin =20 )
    pdf .add_page ()


    pdf .chapter_title ('1. EXECUTIVE SUMMARY & STRATEGIC OVERVIEW')
    pdf .set_font ('Arial','B',12 )
    pdf.set_text_color(33, 33, 33)
    pdf.cell(0, 8, 'Overview:', 0, 1)

    summary_text =(
    f"This report presents a clinical analysis of {stats ['total_restaurants']} restaurant entities in Bangalore. "
    "The objective is to decode the drivers of customer satisfaction and market positioning. "
    f"Key Metrics: Avg Rating ({stats ['avg_rating']:.2f}), Avg Cost/Two ({stats ['avg_cost']:.2f} INR).\n"
    "GitHub Repository: https://github.com/ankushsingh003/IIML.git\n\n"
    "Strategic High-Level Inferences:\n"
    "- Engagement as a Proxy for Quality: High rating reliability is anchored in engagement volume (Votes).\n"
    "- Price Sensitivity: The market is heavily concentrated in the sub-1000 INR price point, indicating a value-driven consumer base.\n"
    "- Digital Maturity: Service features like Online Ordering are no longer 'perks' but operational imperatives for rating stability."
    )
    pdf .add_insight_text (summary_text )
    pdf .ln (5 )


    pdf .chapter_title ('2. UNIVARIATE ANALYSIS: RAW DISTRIBUTIONS')


    img_path =os .path .join (visuals_dir ,'rating_distribution.png')
    if os .path .exists (img_path ):
        pdf .image (img_path ,x =20 ,w =170 )
        pdf .add_insight_text ("INFERENCE: The ratings follow a near-normal distribution skewed towards 3.5. Competition is high in the mid-range (3.2-3.8), meaning restaurants must over-deliver to break into the 4.0+ 'Premium' tier.")
        pdf .ln (5 )


    img_path =os .path .join (visuals_dir ,'cost_distribution.png')
    if os .path .exists (img_path ):
        if pdf .get_y ()>200 :pdf .add_page ()
        pdf .image (img_path ,x =20 ,w =170 )
        pdf .add_insight_text ("INFERENCE: Massive concentration in the 400-800 INR bracket. Scaling for mid-to-high cost ventures requires a very distinct value proposition to justify the 'Price Premium' to cost-conscious Bangaloreans.")
        pdf .ln (5 )


    img_path =os .path .join (visuals_dir ,'top_cuisines.png')
    if os .path .exists (img_path ):
        if pdf .get_y ()>200 :pdf .add_page ()
        pdf .image (img_path ,x =20 ,w =170 )
        pdf .add_insight_text ("INFERENCE: North Indian and Chinese are staples. Market entry in these segments requires efficiency; niche cuisines show lower count but may have untapped loyalty potential.")
        pdf .ln (5 )


    pdf .add_page ()
    pdf .chapter_title ('SECTION 2.1: OPERATIONAL CLASS IMBALANCES')

    for img_name ,inf in [
    ('imbalance_online_order.png',"INFERENCE: High online order adoption indicates a delivery-heavy market. Entities without online presence are likely losing 60%+ market reach."),
    ('imbalance_book_table.png',"INFERENCE: Table booking remains a 'Fine Dining' niche. Most restaurants focus on quick turnaround and high-volume casual customers."),
    ('imbalance_rest_type.png',"INFERENCE: Casual Dining and Delivery setups dominate. The market prefers convenience over slow-format formal dining.")
    ]:
        img_path =os .path .join (visuals_dir ,img_name )
        if os .path .exists (img_path ):
            if pdf .get_y ()>200 :pdf .add_page ()
            pdf .image (img_path ,x =40 ,w =130 )
            pdf .add_insight_text (inf )
            pdf .ln (3 )


    pdf .add_page ()
    pdf .chapter_title ('3. BIVARIATE ANALYSIS: SUCCESS DEPENDENCIES')


    img_path =os .path .join (visuals_dir ,'bivariate_votes_rate.png')
    if os .path .exists (img_path ):
        pdf .image (img_path ,x =20 ,w =170 )
        pdf .add_insight_text ("INFERENCE: Positive correlation between 'Volume of Feedback' and 'Quality of Rating'. Popular restaurants tend to stay popular through social proof mechanisms.")
        pdf .ln (5 )


    img_path =os .path .join (visuals_dir ,'bivariate_location_rate.png')
    if os .path .exists (img_path ):
        if pdf .get_y ()>200 :pdf .add_page ()
        pdf .image (img_path ,x =20 ,w =170 )
        pdf .add_insight_text ("INFERENCE: Geographic Quality Variance. Areas like Indiranagar and Koramangala show tighter high-rating clusters, indicating a more sophisticated and demanding customer base in these hubs.")
        pdf .ln (5 )


    img_path =os .path .join (visuals_dir ,'online_order_ratings.png')
    if os .path .exists (img_path ):
        if pdf .get_y ()>200 :pdf .add_page ()
        pdf .image (img_path ,x =40 ,w =130 )
        pdf .add_insight_text ("INFERENCE: Restaurants offering online ordering consistently show better rating stability and fewer bottom-tier ratings compared to purely offline peers.")
        pdf .ln (5 )


    pdf .add_page ()
    pdf .chapter_title ('4. CORRELATION & FEATURE IMPACT')

    img_path =os .path .join (visuals_dir ,'correlation_heatmap.png')
    if os .path .exists (img_path ):
        pdf .image (img_path ,x =20 ,w =170 )
        pdf .add_insight_text ("INFERENCE: High multi-collinearity between Votes and Ratings. Operational focus should be on driving customer engagement to indirectly lift brand perception.")
        pdf .ln (5 )

    img_path =os .path .join (visuals_dir ,'feature_importance.png')
    if os .path .exists (img_path ):
        if pdf .get_y ()>200 :pdf .add_page ()
        pdf .image (img_path ,x =20 ,w =170 )
        pdf .add_insight_text ("INFERENCE: DECODING SUCCESS. 'Votes' (Engagement) and 'Approx Cost' (Value Strategy) are the top predictors. Service features like Booking/Online are secondary but foundational. Focus: Maximize reviews, optimize price-to-value ratio.")

    pdf .output (output_pdf )
    print (f"Professional Insight Report generated: {output_pdf }")

if __name__ =="__main__":
    df =pd .read_csv ("cleaned_restaurant_data.csv")
    all_cuisines =df ['cuisines'].dropna ().str .split (', ').explode ()
    top_cuisines =all_cuisines .value_counts ().head (3 ).index .tolist ()

    summary_stats ={
    'total_restaurants':len (df ),
    'avg_rating':df ['rate'].mean (),
    'avg_cost':df ['approx_cost(for two people)'].mean (),
    'top_cuisines':top_cuisines 
    }

    create_enhanced_pdf (summary_stats ,"visuals","Restaurant_Market_Analysis_Report.pdf")
