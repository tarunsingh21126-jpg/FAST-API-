import { Bookmark, ArrowUpRight } from "lucide-react";

function JobCard({ job }) {
  const backgroundColors = {
    peach: "bg-[#FDE0CC]",
    green: "bg-[#CFF3E9]",
    purple: "bg-[#E1DAF8]",
    blue: "bg-[#D8EFFB]",
    pink: "bg-[#F8DDF0]",
    gray: "bg-[#E8EDF1]",
  };

  const logoColors = {
    amazon: "bg-black text-white",
    google: "bg-white text-blue-600",
    dribbble: "bg-[#EA4C89] text-white",
    twitter: "bg-[#1DA1F2] text-white",
    airbnb: "bg-[#FF385C] text-white",
    apple: "bg-white text-black",
  };

  return (
    <div className="w-full rounded-[22px] border border-gray-300 bg-white p-2 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-lg">

      {/* Colored Card */}
      <div
        className={`relative min-h-[270px] rounded-[18px] p-4 ${
          backgroundColors[job.bg]
        }`}
      >

        {/* Top Row */}
        <div className="flex items-center justify-between">

          {/* Date */}
          <div className="rounded-full bg-white px-3 py-2 text-xs font-medium text-gray-700 shadow-sm">
            {job.date}
          </div>

          {/* Bookmark */}
          <button
            className="flex h-9 w-9 items-center justify-center rounded-full bg-white text-gray-700 transition hover:bg-gray-100"
            aria-label="Bookmark job"
          >
            <Bookmark size={16} strokeWidth={1.8} />
          </button>
        </div>

        {/* Company */}
        <div className="mt-5">

          <p className="text-xs font-medium text-gray-700">
            {job.company}
          </p>

          <div className="mt-1 flex items-start justify-between gap-3">

            <h2 className="max-w-[180px] text-[21px] font-medium leading-[1.05] tracking-tight text-gray-900">
              {job.title}
            </h2>

            {/* Company Logo */}
            <div
              className={`flex h-20 w-20 shrink-0 items-center justify-center rounded-full text-lg font-bold shadow-sm ${
                logoColors[job.logoType]
              }`}
            >
              {job.logo}
            </div>

          </div>
        </div>

        {/* Tags */}
        <div className="absolute bottom-4 left-4 right-4 flex flex-wrap gap-2">

          {job.tags.map((tag, index) => (
            <span
              key={index}
              className="rounded-full border border-gray-400/60 bg-white/20 px-3 py-1.5 text-[11px] font-medium text-gray-700 backdrop-blur-sm"
            >
              {tag}
            </span>
          ))}

        </div>
      </div>

      {/* Bottom Section */}
      <div className="flex items-center justify-between px-3 pb-2 pt-3">

        {/* Salary + Location */}
        <div>
          <p className="text-sm font-bold text-gray-900">
            {job.salary}
          </p>

          <p className="mt-0.5 text-xs text-gray-400">
            {job.location}
          </p>
        </div>

        {/* Details Button */}
        <button className="flex items-center gap-1 rounded-full bg-[#171717] px-4 py-2.5 text-xs font-medium text-white transition hover:bg-black hover:px-5">
          Details
          <ArrowUpRight size={13} />
        </button>

      </div>
    </div>
  );
}

export default JobCard;