from FirstPhase.labelExtracted import *


def main(output_directory):
    dataset_manager = ResumeDatasetManager()
    print(f"Finished \n {dataset_manager.resumes} ")
    resume_processor = ResumeProcessor()
    for ind in dataset_manager.resumes.index:
        current = ind
        if ind + NUMBER[0] > 2000:
            break
        print(f"Processing resume {ind + NUMBER[0]}")
        try:
            process_and_save(resume_processor,
                             output_directory,
                             dataset_manager.resumes.loc[ind + NUMBER[0]]["Value"],
                             ind + NUMBER[0])
        except:
            NUMBER[0] += current
            raise Exception
    print("finished")


NUMBER = [0]
OUTPUT_FOLDER = r"C:\Users\Hussam Salamh\Desktop\Projects\task\result_with_new_prompt"
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

while True:
    try:
        if NUMBER[0] > 1997:
            break
        main(OUTPUT_FOLDER)
    except:
        continue
    break
